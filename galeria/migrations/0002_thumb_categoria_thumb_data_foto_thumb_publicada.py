# Generated by Django 5.0.4 on 2024-04-15 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumb',
            name='categoria',
            field=models.CharField(choices=[('SIMULAÇÃO', 'Simulação'), ('COOPERATIVO', 'Cooperativo'), ('MUNDO ABERTO', 'Mundo aberto'), ('RougeLike', 'Rougelike')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='thumb',
            name='data_foto',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='thumb',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
