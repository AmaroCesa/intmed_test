from rest_framework import serializers
from .models import Pedido

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    processador = serializers.HyperlinkedIdentityField(view_name='processador')
    memoria = serializers.HyperlinkedIdentityField(view_name='memoria')
    disco = serializers.HyperlinkedIdentityField(view_name='disco')
    placa_video = serializers.HyperlinkedIdentityField(view_name='placa_video')
    gabinete = serializers.HyperlinkedIdentityField(view_name='gabinete')
    placa_mae = serializers.HyperlinkedIdentityField(view_name='placa_mae')
    fonte = serializers.HyperlinkedIdentityField(view_name='fonte')
    class Meta:
        model = Pedido
        fields = ('__all__')