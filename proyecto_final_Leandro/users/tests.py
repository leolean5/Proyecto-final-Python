from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Message

class PruebasUsuarios(TestCase):
    """
    Clase que agrupa las pruebas relacionadas con los usuarios:
    - Registro de usuarios
    - Edición de perfiles
    - Envío y recepción de mensajes
    """
    
    def setUp(self):
        """
        Configuración inicial para las pruebas:
        - Creamos un cliente para simular peticiones.
        - Creamos un usuario de prueba.
        """
        self.client = Client()
        self.usuario_prueba = User.objects.create_user(
            username='usuario_prueba',
            password='1234',
            email='prueba@correo.com'
        )
    
    def test_registro_usuario(self):
        """
        Prueba para verificar que el registro de usuarios funciona correctamente.
        """
        # Datos para un nuevo usuario
        datos_registro = {
            'username': 'nuevo_usuario',
            'password1': '1234',
            'password2': '1234',
            'email': 'nuevo@correo.com'
        }
        
        # Enviamos una petición POST para registrar un usuario
        respuesta = self.client.post(reverse('register'), datos_registro)
        
        # Verificamos que el usuario se haya creado y se redirige correctamente
        self.assertEqual(respuesta.status_code, 302)  # Redirige después del registro
        self.assertTrue(User.objects.filter(username='nuevo_usuario').exists())  # Usuario creado
    
    def test_editar_perfil(self):
        """
        Prueba para verificar que se puede editar un perfil de usuario.
        """
        # Iniciamos sesión con el usuario de prueba
        self.client.login(username='usuario_prueba', password='1234')
        
        # Datos actualizados del perfil
        datos_perfil = {
            'username': 'usuario_actualizado',
            'email': 'nuevo_correo@correo.com',
        }
        
        # Enviamos una petición POST para actualizar el perfil
        respuesta = self.client.post(reverse('editar_perfil'), datos_perfil)
        
        # Refrescamos los datos del usuario y verificamos los cambios
        self.usuario_prueba.refresh_from_db()
        self.assertEqual(self.usuario_prueba.username, 'usuario_actualizado')  # Verifica username
        self.assertEqual(self.usuario_prueba.email, 'nuevo_correo@correo.com')  # Verifica email
    
    def test_envio_mensaje(self):
        """
        Prueba para verificar que se pueden enviar mensajes entre usuarios.
        """
        # Creamos un segundo usuario para enviarle mensajes
        segundo_usuario = User.objects.create_user(
            username='segundo_usuario',
            password='5678',
            email='segundo@correo.com'
        )
        
        # Iniciamos sesión con el primer usuario
        self.client.login(username='usuario_prueba', password='1234')
        
        # Datos del mensaje
        datos_mensaje = {
            'recipient': segundo_usuario.id,
            'content': 'Hola, este es un mensaje de prueba.'
        }
        
        # Enviamos una petición POST para enviar un mensaje
        respuesta = self.client.post(reverse('send_message'), datos_mensaje)
        
        # Verificamos que el mensaje se haya creado
        self.assertEqual(respuesta.status_code, 302)  # Redirige después de enviar el mensaje
        self.assertTrue(Message.objects.filter(content='Hola, este es un mensaje de prueba.').exists())  # Mensaje creado
    
    def test_mensajes_recibidos(self):
        """
        Prueba para verificar que un usuario puede ver los mensajes que ha recibido.
        """
        # Creamos un mensaje enviado al usuario de prueba
        Message.objects.create(
            sender=self.usuario_prueba,
            recipient=self.usuario_prueba,
            content="Este es un mensaje de prueba."
        )
        
        # Iniciamos sesión con el usuario
     
