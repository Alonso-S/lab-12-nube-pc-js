-- Crear base de datos
CREATE DATABASE my_database;

-- Usar esa base de datos
USE my_database;

CREATE TABLE images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    storage_key VARCHAR(255) NOT NULL, -- Nombre interno único del archivo (ej. UUID_nombre.jpg)
    original_filename VARCHAR(255) NOT NULL, -- Nombre del archivo cargado originalmente por el usuario
    mime_type VARCHAR(100), -- Tipo de contenido: image/png, image/jpeg, etc.
    uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    uploader_ip VARCHAR(45) -- IP del cliente que hizo la carga
);