from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Ruta para el registro de usuarios
    path('profile/', views.profile, name='profile'),  # Ruta para visualizar el perfil
    path('profile/edit/', views.editar_perfil, name='editar_perfil'),  # Editar perfil
    path('profile/password/', views.cambiar_contrasena, name='cambiar_contrasena'),  # Cambiar contraseña
    path('messages/', views.message_list, name='message_list'),  # Lista de mensajes
    path('messages/<int:message_id>/', views.message_detail, name='message_detail'),  # Detalle de mensaje
    path('messages/send/', views.send_message, name='send_message'),  # Enviar mensaje
]
