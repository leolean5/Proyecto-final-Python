from django.db import models  # Importamos las herramientas necesarias para definir modelos
from django.contrib.auth.models import User  # Importamos el modelo de usuarios de Django para relacionarlo con los blogs

# Definimos el modelo Blog, que representará cada entrada en nuestro blog
class Blog(models.Model):
    title = models.CharField(max_length=200)  # Título del blog, con un límite de 200 caracteres
    subtitle = models.CharField(max_length=200, blank=True)  # Subtítulo opcional (blank=True permite que sea vacío)
    body = models.TextField()  # Cuerpo del blog, donde irá el contenido principal
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User. Cada blog tendrá un autor. Si se elimina el autor, se elimina su blog
    date = models.DateField(auto_now_add=True)  # Fecha de creación automática al guardar el blog por primera vez
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Imagen opcional del blog. Se guardará en la carpeta 'blog_images/'

    def __str__(self):  
        # Método para mostrar una representación legible del blog (en este caso, su título)
        return self.title


