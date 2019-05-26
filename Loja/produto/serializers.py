from .models import Produto
from rest_framework import serializers
from pedido.serializer import ProdutoSerializer

class ProdutoSerializer(serializers.ModelSerializer):
    pedido_list = ProdutoSerializer(many=True, read_only=True)
    class Meta:
        model = Produto
        fields = ('url', 'especificacoes', 'preco', 'categoria', 'pedido_list')






