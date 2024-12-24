from django import forms
from .models import Blog

# Formulario basado en el modelo Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog  # Usamos el modelo Blog
        fields = ['title', 'subtitle', 'body', 'author', 'image']  # Campos que estarán en el formulario
