from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Evento(models.Model):#crio uma classe especificando como eu quero minha tabela
    titulo=models.CharField(max_length=100)
    descricao=models.TextField(blank=True, null=True)
    data_evento=models.DateTimeField(verbose_name='Data do Evento')
    data_criacao=models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table='evento'

    def __str__(self):#quero que apareça o título do evento na listagem
        return self.titulo