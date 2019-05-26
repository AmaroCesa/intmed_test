from rest_framework import serializers
from .models import Pedido
from produto.models import Produto

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), many=True)

    class Meta:
        model = Pedido
        fields = ('__all__')


