from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ImageRecord(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    storage_key = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    mime_type = db.Column(db.String(100))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    uploader_ip = db.Column(db.String(45))
