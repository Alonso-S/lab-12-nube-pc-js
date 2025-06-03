# 🖼️ Galería de Imágenes Moderna

Una aplicación web desarrollada con **Flask** que permite a los usuarios subir,
visualizar y gestionar imágenes utilizando **AWS S3** como almacenamiento y
**MySQL** para la metadata. Perfecta para crear galerías personales o
profesionales con almacenamiento en la nube.

## ✨ Características

- ⬆️ Subida de imágenes con validación de formato
- ☁️ Almacenamiento seguro en AWS S3
- 🗄️ Metadata almacenada en MySQL
- 🖥️ Interfaz web moderna y responsive
- 🗑️ Eliminación de imágenes (S3 + base de datos)
- 📊 Registro de IP y fecha de subida
- 🔄 Listado ordenado por fecha

## 🧱 Requisitos Previos

- **Python 3.10+**
- **MySQL Server** (local o remoto)
- **Cuenta de AWS** con bucket S3 configurado
- **Git** para clonar el repositorio
- Acceso a internet para conexión con AWS

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Alonso-S/lab-12-nube-pc-js
cd lab-12-nube-pc-js
```

### 2. Crear y activar entorno virtual

**En Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

> 💡 **Importante:** Siempre activa el entorno virtual antes de trabajar con el
> proyecto.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
# Base de datos
DATABASE_URI=mysql://usuario:contraseña@localhost/my_database

# AWS Credentials
AWS_ACCESS_KEY_ID=tu_clave_de_acceso
AWS_SECRET_ACCESS_KEY=tu_clave_secreta
AWS_REGION=us-east-1
AWS_BUCKET_NAME=tu-nombre-de-bucket
```

> ⚠️ **Seguridad:** Nunca subas el archivo `.env` al repositorio. Ya está
> incluido en `.gitignore`.

### 5. Configurar la base de datos

Ejecuta el siguiente script SQL en tu servidor MySQL:

```sql
-- Crear base de datos
CREATE DATABASE my_database;

-- Usar la base de datos
USE my_database;

-- Crear tabla de imágenes
CREATE TABLE images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    storage_key VARCHAR(255) NOT NULL,
    original_filename VARCHAR(255) NOT NULL,
    mime_type VARCHAR(100),
    uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    uploader_ip VARCHAR(45)
);
```

### 6. Configurar AWS S3

1. Crea un bucket en AWS S3
2. Configura las políticas de acceso apropiadas
3. Asegúrate de que tu usuario AWS tenga permisos para:
   - `s3:PutObject`
   - `s3:GetObject`
   - `s3:DeleteObject`

## 🚀 Ejecución

1. **Activa el entorno virtual** (si no está activado):
   ```bash
   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

2. **Inicia la aplicación:**
   ```bash
   python app.py
   ```

3. **Abre tu navegador en:** `http://localhost:5000`

## 📁 Estructura del Proyecto

```
lab-12-nube-pc-js/
├── app.py                 # Aplicación principal Flask
├── models.py             # Modelos de base de datos
├── requirements.txt      # Dependencias Python
├── .env                 # Variables de entorno (no incluido)
├── .gitignore          # Archivos ignorados por Git
├── templates/
│   └── index.html      # Interfaz web
├── mysql-init/
│   └── init.sql       # Script de inicialización DB
└── venv/              # Entorno virtual (no incluido)
```

## 🔧 Uso

1. **Subir imagen:** Selecciona una imagen desde la interfaz web
2. **Ver galería:** Las imágenes se muestran automáticamente
3. **Eliminar imagen:** Haz clic en el botón eliminar junto a cada imagen

### Formatos soportados

- JPG/JPEG
- PNG
- GIF
- WEBP
- BMP

## 🔐 Variables de Entorno

| Variable                | Descripción          | Ejemplo                                    |
| ----------------------- | -------------------- | ------------------------------------------ |
| `DATABASE_URI`          | Conexión a MySQL     | `mysql://user:pass@localhost/db`           |
| `AWS_ACCESS_KEY_ID`     | Clave de acceso AWS  | `AKIAIOSFODNN7EXAMPLE`                     |
| `AWS_SECRET_ACCESS_KEY` | Clave secreta AWS    | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `AWS_REGION`            | Región del bucket    | `us-east-1`                                |
| `AWS_BUCKET_NAME`       | Nombre del bucket S3 | `mi-galeria-imagenes`                      |

## 🛠️ Desarrollo

### Desactivar entorno virtual

```bash
deactivate
```

### Actualizar dependencias

```bash
pip freeze > requirements.txt
```

## 🚨 Solución de Problemas

**Error de conexión a MySQL:**

- Verifica que MySQL esté ejecutándose
- Confirma las credenciales en `.env`

**Error de permisos AWS:**

- Verifica las credenciales AWS
- Confirma los permisos del bucket S3

**Módulos no encontrados:**

- Asegúrate de haber activado el entorno virtual
- Reinstala las dependencias: `pip install -r requirements.txt`
