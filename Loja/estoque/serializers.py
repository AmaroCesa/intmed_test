from rest_framework import serializers
from .models import Estoque

class EstoqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estoque
        fields = ('__all__')
