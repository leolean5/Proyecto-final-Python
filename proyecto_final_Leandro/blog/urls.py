from django.urls import path  # Importo la herramienta para manejar rutas
from . import views  # Importo las vistas del blog

# Rutas de la app blog
urlpatterns = [
    path('', views.blog_lista, name='blog_lista'),  # Lista de publicaciones
    path('<int:blog_id>/', views.blog_detalle, name='blog_detalle'),  # Detalles de una publicación
    path('crear/', views.blog_crear, name='blog_crear'),  # Crear publicación
    path('<int:blog_id>/editar/', views.blog_editar, name='blog_editar'),  # Editar publicación
    path('<int:blog_id>/eliminar/', views.blog_eliminar, name='blog_eliminar'),  # Eliminar publicación
]
