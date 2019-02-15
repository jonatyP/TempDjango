from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)

class Cliente(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cpf', 'telefone', 'email']
