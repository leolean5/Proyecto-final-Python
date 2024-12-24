from django.urls import path  # Importo la herramienta para manejar rutas
from . import views  # Importo las vistas del blog

# Defino las rutas de la app blog
urlpatterns = [
    path('', views.blog_lista, name='blog_lista'),  # Ruta para listar publicaciones (Pagina principal)
    path('<int:blog_id>/', views.blog_detalle, name='blog_detalle'),  # Ruta para mostrar detalles de una publicación específica (por su ID)
]

