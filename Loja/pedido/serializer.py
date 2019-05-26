from rest_framework import serializers
from .models import Pedido
from produto.models import Produto

class PedidoSerializer(serializers.ModelSerializer):
    produtos = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), many=True)

    class Meta:
        model = Pedido
        fields = ('id', 'valor','cliente', 'statu_pedido', 'produtos')


