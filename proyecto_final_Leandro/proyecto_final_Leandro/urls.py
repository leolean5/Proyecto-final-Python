from django.contrib import admin
from django.urls import path, include  # Importamos include para usar rutas predefinidas de Django
from django.contrib.auth import views as auth_views  # Importamos vistas genéricas de Django

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('', include('blog.urls')),  # Incluye las rutas del blog
    path('accounts/', include('users.urls')),  # Incluye rutas personalizadas de registro y perfiles
    path('accounts/', include('django.contrib.auth.urls')),  # Rutas estándar para login, logout, password_reset, etc.
]

