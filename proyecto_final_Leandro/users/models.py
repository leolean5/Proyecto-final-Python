from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)  # Usuario que envía
    recipient = models.ForeignKey(User, related_name="recipient_messages", on_delete=models.CASCADE)  # Usuario que recibe
    content = models.TextField()  # Contenido del mensaje
    timestamp = models.DateTimeField(auto_now_add=True)  # Fecha y hora en que se envió

    def __str__(self):
        return f"De {self.sender.username} a {self.recipient.username} - {self.timestamp}"
