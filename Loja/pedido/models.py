from django.db import models
from produto.models import Produto

# Create your models here.
class Pedido(models.Model):    
    
    Pedido Realizado
    Separação em estoque
    Em montagem
    Realização de testes
    Concluído
    
    valor = models.FloatField()
    statu_pedido = models.CharField(max_length=20)
    processador = models.OneToOneField(Produto)
    MEMORIARAM = models.OneToOneField(Produto)
    DISCORIGIDO = models.OneToOneField(Produto)
    PLACAVIDEO = models.OneToOneField(Produto)
    GABINETE = models.OneToOneField(Produto)
    PLACAMAE = models.OneToOneField(Produto)
    FONTE = models.OneToOneField(Produto)
