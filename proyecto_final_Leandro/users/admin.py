from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp')  # Muestra campos clave en el admin
    list_filter = ('timestamp',)  # Permite filtrar por fecha
    search_fields = ('sender__username', 'receiver__username', 'content')  # Busca en usuarios y contenido