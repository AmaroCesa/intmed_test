from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status

from .models import Produto
from .models import Categoria
from .serializers import ProdutoSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from estoque.models import Estoque
# Create your views here.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer 

    def create(self, validate_data):
        """
            Alteração do create para inserir em estoque o produto cadastrado
        """
        serializer = ProdutoSerializer(data=validate_data.data, context=validate_data.data.dict())
        if serializer.is_valid():
            produto = serializer.save()
            Estoque.objects.create(produto=produto, quantidade_em_estoque=0,quantidade_venda=0)
            
            return Response(serializer.context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        # import ipdb; ipdb.set_trace()
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    