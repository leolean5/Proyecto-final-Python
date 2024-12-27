from django.shortcuts import render, redirect, get_object_or_404  # Para renderizar plantillas y redirigir
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm  # Formulario prediseñados
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages  # Para mostrar mensajes de éxito o error
from django.contrib.auth.decorators import login_required  # Para requerir autenticación
from .forms import EditarPerfilForm, MessageForm, RegistroForm  # Importamos formularios creados
from .models import Message
from django.contrib.auth.models import User


# Vista para registrar usuarios
def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el nuevo usuario
            username = user.username  # Obtén el nombre de usuario
            messages.success(request, f'¡Tu cuenta ha sido creada, {username}! Ya puedes iniciar sesión.')
            return render(request, 'users/registration_success.html', {'username': username})
    else:
        form = RegistroForm()
    return render(request, 'users/register.html', {'form': form})

# Vista para mostrar el perfil de usuario
@login_required  # Requiere que el usuario esté autenticado
def profile(request):
    return render(request, 'users/profile.html')  # Renderiza la página de perfil

# Vista para editar el perfil
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('profile')  # Redirige al perfil tras guardar
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'users/editar_perfil.html', {'form': form})

# Vista para cambiar la contraseña
@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Mantener al usuario autenticado después del cambio
            messages.success(request, '¡Tu contraseña ha sido actualizada con éxito!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/cambiar_contrasena.html', {'form': form})

# Lista los mensajes enviados y recibidos por el usuario autenticado
@login_required
def message_list(request):
    mensajes_recibidos = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    mensajes_enviados = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'messages/message_list.html', {
        'mensajes_recibidos': mensajes_recibidos,
        'mensajes_enviados': mensajes_enviados,
    })

# Detalle de un mensaje específico
@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if message.recipient != request.user and message.sender != request.user:
        messages.error(request, "No tienes permiso para ver este mensaje.")
        return redirect('message_list')
    return render(request, 'messages/message_detail.html', {'message': message})

    # Formulario para enviar un nuevo mensaje
@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.sender = request.user  # Establecemos al usuario logueado como remitente
            mensaje.save()
            messages.success(request, 'Mensaje enviado con éxito!')
            return redirect('message_list')  # Redirigir a la lista de mensajes
    else:
        form = MessageForm()
    return render(request, 'messages/send_message.html', {'form': form})




