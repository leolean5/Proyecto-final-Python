from django.shortcuts import render, get_object_or_404  # Importamos herramientas para renderizar y manejar errores
from .models import Blog  # Importamos el modelo Blog para interactuar con la base de datos

# Vista para listar todas las publicaciones
def blog_lista(request):
    publicaciones = Blog.objects.all().order_by('-date')  
    # Obtengo todas las publicaciones, ordenadas por fecha descendente
    return render(request, 'blog/blog_lista.html', {'publicaciones': publicaciones})  
    # Renderizo la plantilla blog_lista.html y le paso las publicaciones como contexto

# Vista para mostrar los detalles de una publicación específica
def blog_detalle(request, blog_id):
    publicacion = get_object_or_404(Blog, id=blog_id)  
    # Busco una publicación por ID. Si no existe, devuelvo un error 404
    return render(request, 'blog/blog_detalle.html', {'publicacion': publicacion})  
    # Renderizo la plantilla blog_detalle.html y le paso la publicación como contexto

