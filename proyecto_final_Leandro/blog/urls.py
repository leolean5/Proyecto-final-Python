from django.urls import path
from . import views  # Importamos las vistas

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página principal
]
