
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Estoque
from produto.models import Produto
from .serializers import EstoqueSerializer
from django.forms.models import model_to_dict

class EstoqueView(generics.RetrieveUpdateAPIView):
  
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EstoqueSerializer(queryset, many=True)
        return Response(serializer.data)    
 
    def update(self, request, *arg, **kwargs):
        """
            Inserir quantidade de produtos a serem vendidos
        """
        produto = Produto.objects.filter(id=request.data['prodoto_pk']).first()
        if produto :
            estoque = Estoque.objects.filter(produto=produto).first()
            estoque.quantidade_em_estoque += request.data.get('quantidade_em_estoque', 0)
            estoque.quantidade_venda += request.data.get('quantidade_venda', 0)
            
            try :
                estoque.save()
            except e:
                return Response({'detail': e}, status=status.HTTP_400_BAD_REQUEST)
            return Response(model_to_dict(estoque), status=status.HTTP_200_OK)
        return Response({'detail': 'Produto Inesistente'}, status=status.HTTP_400_BAD_REQUEST)
