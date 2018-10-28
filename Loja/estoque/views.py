
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Estoque
from .serializers import EstoqueSerializer
from django.forms.models import model_to_dict

class EstoqueView(generics.RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    generics.RetrieveUpdateAPIView

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EstoqueSerializer(queryset, many=True)
        return Response(serializer.data)    
 
    def update(self, request, *arg, **kwargs):
        """
            Inserir quantidade de produtos a serem vendidos
        """
        produto = request.data['prodoto_pk']
        if produto :
            estoque = Estoque.objects.filte(produto=produto)
            estoque.quantidade_em_estoque += request.data.get('quantidade_em_estoque', 0)
            estoque.quantidade_venda += request.data.get('quantidade_venda', 0)
            try :
                estoque.save()
            except e:
                return Response({'detail': e}, status=status.HTTP_400_BAD_REQUEST)
            return Response(model_to_dict(estoque), status=status.HTTP_200_OK)
        return Response({'detail': 'Produto Inesistente'}, status=status.HTTP_400_BAD_REQUEST)
