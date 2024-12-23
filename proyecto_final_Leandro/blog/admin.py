from django.contrib import admin  # Importamos las herramientas necesarias para registrar modelos en el admin
from .models import Blog  # Importamos el modelo Blog

# Registramos el modelo Blog para que pueda ser gestionado desde el panel de administración
admin.site.register(Blog)
