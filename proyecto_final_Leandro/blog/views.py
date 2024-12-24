from django.shortcuts import render, get_object_or_404, redirect  # Importamos herramientas para renderizar y manejar errores
from .models import Blog  # Importamos el modelo Blog para interactuar con la base de datos
from .forms import BlogForm # Importamos el formulario
from django.contrib import messages  # Importo el sistema de mensajes
from django.contrib.auth.decorators import login_required  # Para requerir autenticación
from django.core.exceptions import PermissionDenied  # Para manejar permisos de usuario


# Vista para listar todas las publicaciones
def blog_lista(request):
    blogs = Blog.objects.all().order_by('-date')  
    # Traemos todas las publicaciones ordenadas por fecha descendente
    return render(request, 'blog/blog_lista.html', {'blogs': blogs})  
    # Pasamos las publicaciones al template como 'blogs'

# Vista para mostrar los detalles de una publicación específica
def blog_detalle(request, blog_id):
    publicacion = get_object_or_404(Blog, id=blog_id)  
    # Busco una publicación por ID. Si no existe, devuelvo un error 404
    return render(request, 'blog/blog_detalle.html', {'publicacion': publicacion})  
    # Renderizo la plantilla blog_detalle.html y le paso la publicación como contexto


# Vista para crear una nueva publicación
@login_required  # Solo usuarios autenticados pueden crear publicaciones
def blog_crear(request):
    if request.method == 'POST':
        formulario = BlogForm(request.POST, request.FILES)  # Procesa los datos enviados en el formulario
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.author = request.user  # Asigna automáticamente el autor autenticado
            publicacion.save()
            # Agrega un mensaje de confirmación al crear la publicación
            messages.success(request, '¡La publicación fue creada con éxito!')
            return redirect('blog_lista')  # Redirige a la lista de publicaciones
    else:
        formulario = BlogForm()  # Renderiza un formulario vacío si es GET
    return render(request, 'blog/blog_form.html', {'formulario': formulario})

# Vista para editar una publicación existente
@login_required  # Solo usuarios autenticados pueden editar publicaciones
def blog_editar(request, blog_id):
    publicacion = get_object_or_404(Blog, id=blog_id)
    if request.user != publicacion.author:
        # Solo el autor puede editar su publicación
        raise PermissionDenied
    if request.method == 'POST':
        formulario = BlogForm(request.POST, request.FILES, instance=publicacion)
        if formulario.is_valid():
            formulario.save()
            # Agrega un mensaje de confirmación al editar la publicación
            messages.success(request, '¡La publicación fue editada con éxito!')
            return redirect('blog_lista')
    else:
        formulario = BlogForm(instance=publicacion)  # Renderiza el formulario con la instancia actual
    return render(request, 'blog/blog_form.html', {'formulario': formulario})

# Vista para eliminar una publicación
@login_required  # Solo usuarios autenticados pueden eliminar publicaciones
def blog_eliminar(request, blog_id):
    publicacion = get_object_or_404(Blog, id=blog_id)
    if request.user != publicacion.author:
        # Solo el autor puede eliminar su publicación
        raise PermissionDenied
    if request.method == 'POST':
        publicacion.delete()
        # Agrega un mensaje de confirmación al eliminar la publicación
        messages.success(request, '¡La publicación fue eliminada con éxito!')
        return redirect('blog_lista')
    return render(request, 'blog/blog_eliminar.html', {'publicacion': publicacion})


# Vista para la página "Acerca de mí"
def acerca(request):
    return render(request, 'blog/acerca.html')
    # Renderiza el template acerca.html


