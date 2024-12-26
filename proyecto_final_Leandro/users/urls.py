from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Ruta para el registro de usuarios
    path('profile/', views.profile, name='profile'),  # Ruta para visualizar el perfil
    path('profile/edit/', views.editar_perfil, name='editar_perfil'),  # Editar perfil
    path('profile/password/', views.cambiar_contrasena, name='cambiar_contrasena'),  # Cambiar contraseña
]
