from django.shortcuts import render, redirect  # Para renderizar plantillas y redirigir
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm  # Formulario prediseñados
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages  # Para mostrar mensajes de éxito o error
from django.contrib.auth.decorators import login_required  # Para requerir autenticación
from .forms import EditarPerfilForm  # Importamos formulario creados

# Vista para registrar usuarios
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Tu cuenta ha sido creada, {username}! Ya puedes iniciar sesión.')
            return redirect('login')  # Redirige al login después del registro
    else:
        form = UserCreationForm()  # Si no es POST, muestra un formulario vacío
    return render(request, 'users/register.html', {'form': form})  # Renderiza el formulario de registro

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

