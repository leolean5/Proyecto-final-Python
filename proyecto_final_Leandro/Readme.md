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
5. Accede a la aplicación
    - Página principal del blog: http://127.0.0.1:8000/
    - Panel de administración: http://127.0.0.1:8000/admin/

## Funcionalidades implementadas
1. Autenticación de usuarios:
   - Iniciar sesión: Ruta /login/
   -Cerrar sesión: Botón "Cerrar Sesión" en la barra de navegación.
2. CRUD de publicaciones:
   - Crear publicaciones: Ruta /crear/
   - Editar publicaciones: Ruta /<id_de_publicacion>/editar/
   - Eliminar publicaciones: Ruta /<id_de_publicacion>/eliminar/
3. Manejo de imágenes:
   - Cada publicación puede incluir una imagen asociada.
4. Mensajes de confirmación:
   - Mensajes claros al realizar acciones como crear, editar o eliminar publicaciones.
5. Diseño básico con HTML:
   - Estructura sencilla para navegación y vistas de publicaciones.

## TESTs
## TESTs
# App blog

Contiene pruebas para verificar las funcionalidades principales
relacionadas con la aplicación de blog: visualización de publicaciones, 
creación y edición de publicaciones. Las pruebas aseguran que cada 
parte del sistema del blog funcione como se espera.

Pruebas incluidas:
1. Visualización de la lista de publicaciones.
2. Creación de una nueva publicación.
3. Edición de una publicación existente.

- setUp: Configura un cliente, un usuario y una publicación de prueba para las pruebas.
- test_pagina_lista_publicaciones: Verifica que se pueda visualizar la lista de publicaciones.
- test_crear_publicacion_autenticado: Comprueba que se pueden crear nuevas publicaciones.
- test_editar_publicacion: Valida que se puedan editar publicaciones existentes.

Ejecución: `python manage.py test blog`

# App users
Contiene pruebas para verificar las funcionalidades principales
relacionadas con los usuarios: registro, inicio de sesión, edición de perfil
y otros elementos clave de la aplicación. Las pruebas aseguran que cada parte
del sistema de usuarios funciona como se espera.
Pruebas incluidas:
1. Registro de usuario.
2. Inicio de sesión.
3. Edición de perfil.
- setUp: Configura un cliente y un usuario de prueba para las pruebas.
- test_registro_usuario: Verifica que se puedan registrar nuevos usuarios.
- test_editar_perfil: Comprueba que los datos del perfil de un usuario se pueden actualizar.
- test_envio_mensaje: Prueba el envío de mensajes entre usuarios.
- test_mensajes_recibidos: Confirma que los mensajes recibidos aparecen en la lista de mensajes.

Ejecución: `python manage.py test users`


## Notas adicionales
Este proyecto fue probado con Python 3.13 y Django 5.1.4.
Se aclara que en este proyecto tuve ayuda de mi hermano (Ing. en Sistemas) y se utilizo IA para agilizar la realización.

## Autor
Leandro Agustín Molina
Curso de Python - Coderhouse
https://github.com/leolean

