from django.contrib import admin
from django.urls import path, include  # Importamos include para usar rutas predefinidas de Django
from django.contrib.auth import views as auth_views  # Importamos las vistas genéricas de autenticación

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('', include('blog.urls')),  # Incluye las rutas del blog
    path('login/', auth_views.LoginView.as_view(template_name='registracion/login.html'), name='login'),
    # Ruta para login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Ruta para logout
]

