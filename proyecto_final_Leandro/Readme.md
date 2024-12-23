# Proyecto Final - Blog en Django

Este es un proyecto final desarrollado por Leandro Agustín Molina como parte del curso de Python de Coderhouse, cuyo objetivo es construir un blog funcional utilizando Django. El proyecto incluye funcionalidades como autenticación de usuarios, CRUD de entradas del blog y manejo de imágenes.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas y herramientas:

1. **Python** (versión 3.8 o superior)
   - Verificar instalación: `python --version`
2. **Git** (para control de versiones)
   - Verificar instalación: `git --version`
3. **Django** (Framework web)
   - Instalar Django: `python -m pip install django`
   - Verificar instalación: `python -m django --version`
4. **Pillow** (para manejar imágenes en Django)
   - Instalar Pillow: `python -m pip install Pillow`

## Configuración e instalación

1. Clona el repositorio del proyecto:
   ```bash
   git clone https://github.com/leolean5/Proyecto-final-Python.git
   cd proyecto_final_Leandro
2. Migrar la base de datos Aplicá las migraciones necesarias para configurar la base de datos:
    - python manage.py makemigrations
    - python manage.py migrate
3. Crear un superusuario Creá un usuario administrador para acceder al panel de administración:
    - python manage.py createsuperuser
4. Iniciar el servidor Ejecutá el servidor de desarrollo:
    - python manage.py runserver


