from .models import Produto
from rest_framework import serializers

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ('url', 'especificacoes', 'preco')

    