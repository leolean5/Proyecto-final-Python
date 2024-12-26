from django.shortcuts import render, redirect  # Para renderizar plantillas y redirigir
from django.contrib.auth.forms import UserCreationForm  # Formulario prediseñado para registro
from django.contrib import messages  # Para mostrar mensajes de éxito o error
from django.contrib.auth.decorators import login_required  # Para requerir autenticación

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
