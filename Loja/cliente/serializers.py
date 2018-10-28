from rest_framework import serializers
from .models import Cliente 

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Cliente
        fields = ('url','username', 'email', 'telefone', 'password')





  