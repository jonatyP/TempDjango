from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('cpf', max_length=30)
    telefone = models.CharField('Telefone', max_length=11)
    endereco =models.CharField('Endereço', max_length=100)
    email = models.EmailField('Email')
    data = models.DateTimeField('Data', auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'cliente'
