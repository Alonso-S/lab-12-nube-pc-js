import os
import uuid
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from models import db, ImageRecord
import boto3
from botocore.exceptions import BotoCoreError, ClientError

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 280, 
    "pool_pre_ping": True,
}

db.init_app(app)

# Configurar cliente de S3
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

s3 = boto3.client(
    "s3",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")
        if file:
            filename = f"{uuid.uuid4().hex}_{file.filename}"
            try:
                s3.upload_fileobj(
                    Fileobj=file,
                    Bucket=BUCKET_NAME,
                    Key=filename,
                    ExtraArgs={"ContentType": file.content_type}
                )
                new_image = ImageRecord(
                    storage_key=filename,
                    original_filename=file.filename,
                    mime_type=file.content_type,
                    uploader_ip=request.remote_addr
                )
                db.session.add(new_image)
                db.session.commit()
            except (BotoCoreError, ClientError) as e:
                print("Error al subir o registrar imagen:", e)
                return "Error interno", 500
            return redirect(url_for("index"))

    images = ImageRecord.query.order_by(ImageRecord.uploaded_at.desc()).all()
    images_with_url = []
    for img in images:
        url = f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{img.storage_key}"
        images_with_url.append({
            "id": img.id,
            "original_filename": img.original_filename,
            "mime_type": img.mime_type,
            "uploaded_at": img.uploaded_at,
            "uploader_ip": img.uploader_ip,
            "url": url
        })

    return render_template("index.html", images=images_with_url, title="Galería de Imágenes Moderna")




@app.route("/delete/<int:image_id>", methods=["POST"])
def delete_image(image_id):
    image = ImageRecord.query.get_or_404(image_id)

    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=image.storage_key)
    except (BotoCoreError, ClientError) as e:
        print(f"Error al eliminar imagen de S3: {e}")

    db.session.delete(image)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
