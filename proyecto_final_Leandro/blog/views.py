from django.shortcuts import render  # Importamos render para renderizar templates

# Vista para la página principal del blog
def home(request):
    return render(request, 'home.html')  # Renderizamos el template 'home.html'

