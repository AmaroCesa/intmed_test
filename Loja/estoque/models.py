from django.db import models
from .models import Produto

# Create your models here.
class Estoque (models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CACADE)
    quantidade_em_estoque= models.PositiveIntegerField(blank=True, null=True)
    quantidade_venda = models.PositiveIntegerField(blank=True, null=True)