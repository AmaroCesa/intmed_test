from django.db import models
from produto.models import Produto
from cliente.models import Cliente

# Create your models here.
class Pedido(models.Model):    
    """
        Pedido Inconpelto 
        Garantir categoria de cada produto
    """
    
    valor = models.FloatField()
    cliente =  models.ForeignKey(Cliente,related_name=cliente_pedido,on_delete=models.CASCADE)
    statu_pedido = models.CharField(max_length=20)
    processador = models.OneToOneField(Produto, on_delete=models.DO_NOTHING)
    memoria = models.OneToOneField(Produto, on_delete=models.DO_NOTHING)
    disco = models.OneToOneField(Produto, on_delete=models.DO_NOTHING)
    placa_video = models.OneToOneField(Produto, on_delete=models.DO_NOTHING)
    gabinete = models.OneToOneField(Produto, on_delete=models.DO_NOTHING)
    placa_mae = models.OneToOneField(Produto, on_delete=models.DO_NOTHING)
    fonte = models.OneToOneField(Produto, on_delete=models.DO_NOTHING)

