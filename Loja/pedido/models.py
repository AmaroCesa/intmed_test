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
    cliente =  models.ForeignKey(Cliente,related_name='cliente_pedido',on_delete=models.CASCADE)
    statu_pedido = models.CharField(max_length=20)
    produtos = models.ManyToManyField(Produto, related_name="produto_list")
    




