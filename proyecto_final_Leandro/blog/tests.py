from django.test import TestCase, Client
from django.urls import reverse
from .models import Blog
from django.contrib.auth.models import User


class BlogTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')  # Loguear al usuario de prueba

        # Crear una publicación de prueba
        self.blog = Blog.objects.create(
            title="Título de prueba",
            subtitle="Subtítulo de prueba",
            body="Cuerpo de prueba",
            author=self.user,
        )


    def test_pagina_lista_publicaciones(self):
        # Prueba para la página de lista de publicaciones
        response = self.client.get(reverse('blog_lista'))  # Accede a la ruta de la lista de publicaciones
        self.assertEqual(response.status_code, 200)  # Verifica que la página cargue correctamente
        self.assertContains(response, "Título de prueba")  # Verifica que el título del blog esté en la página

    def test_crear_publicacion_autenticado(self):
        self.client.login(username='testuser', password='12345')  # Inicia sesión con el usuario de prueba
        response = self.client.post(reverse('blog_crear'), {
            'title': 'Nuevo título',
            'subtitle': 'Nuevo subtítulo',
            'body': 'Nuevo cuerpo',
        })  # Envía datos para crear una nueva publicación
        self.assertEqual(response.status_code, 302)  # Verifica que redirige después de crear
        self.assertTrue(Blog.objects.filter(title="Nuevo título").exists())  # Verifica que la publicación se creó



    def test_editar_publicacion(self):
        self.client.login(username='testuser', password='12345')  # Inicia sesión con el usuario de prueba
        response = self.client.post(reverse('blog_editar', args=[self.blog.id]), {
            'title': 'Título actualizado',
            'subtitle': self.blog.subtitle,
            'body': self.blog.body,
        })  # Envía datos para actualizar la publicación
        self.assertEqual(response.status_code, 302)  # Verifica que redirige después de editar
        self.blog.refresh_from_db()  # Refresca los datos de la base de datos
        self.assertEqual(self.blog.title, 'Título actualizado')  # Verifica que el título fue actualizado


