from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Thumb(models.Model):

    OPCOES_CATEGORIA = [
        ("SIMULAÇÃO", "Simulação"),
        ("COOPERATIVO", "Cooperativo"),
        ("MUNDO ABERTO" , "Mundo aberto"),
        ("RougeLike", "Rougelike"),
    ]


    nome = models.CharField(max_length=100, null=False, blank=False)
    plataforma = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    publicada = models.BooleanField(default=False)
    data_foto = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self):
        return self.nome