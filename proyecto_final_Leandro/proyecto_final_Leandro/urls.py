from django.contrib import admin
from django.urls import path, include  # Importamos include para conectar las URLs de las apps

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('', include('blog.urls')),  # Conecta la app 'blog' a la URL base
]

