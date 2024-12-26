from django.urls import path
from . import views  # Importamos nuestras vistas personalizadas

urlpatterns = [
    path('register/', views.register, name='register'),  # Ruta para el registro de usuarios
    path('profile/', views.profile, name='profile'),  # Ruta para visualizar el perfil
]
