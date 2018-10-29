from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.'

PROCESADORES = 'Processadores'
MEMORIARAM = 'Memória RAM'
DISCORIGIDO = 'Disco Rígido/SSD'
PLACAVIDEO = 'Placa de Vídeo'
GABINETE = 'Gabinete'
PLACAMAE = 'Placa mãe'
FONTE = 'Fonte'
categoria_validator = (
        PROCESADORES,
        MEMORIARAM,
        DISCORIGIDO,
        PLACAVIDEO,
        GABINETE,
        PLACAMAE,
        FONTE,
    )       

def categoria_range(value):
    if not (value in categoria_validator):
        raise ValidationError(
            'categoria não é valida',
            params={'value': value},
        )
"""
validator para garantir range de categorias
"""
class Categoria(models.Model):
     
    choice_categoria = (
        ('Processadores', PROCESADORES),
        ('Memória RAM', MEMORIARAM),
        ('Disco Rígido/SSD',DISCORIGIDO),
        ('Placa de Vídeo',PLACAVIDEO),
        ('Gabinete',GABINETE),
        ('Placa mãe',PLACAMAE),
        ('Fonte',FONTE)
    )
    categoria_desc = models.CharField(max_length=32, choices=choice_categoria, validators=[categoria_range] )

class Produto (models.Model):
        
    especificacoes = models.TextField(max_length=250, blank=True, null=True)
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
