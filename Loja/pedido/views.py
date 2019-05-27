import json
# from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from produto.models import Categoria
from .trello import create_card
from .serializer import PedidoSerializer
from .models import Pedido


@csrf_exempt
def trello_callback(request, *args, **kwargs):
    #TODO: tratar status pedido verificando mensagem callback
    jsondata = request.body
    try:
        data = json.loads(jsondata)
        action = data['action']['data']
        if action or action != {}:
            pedido_id = action['card']['name'].split(' ')[1]
            pedido = Pedido.objects.filter(pk=pedido_id).first()
            status = action['listAfter']['name']
            pedido.statu_pedido = status
            pedido.save()
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=200)

def check_pedido_valid(pedido):
    categoria = Categoria.objects.all()
    categoria_list = list(categoria)
    lista_verificar = []
    for cat in categoria_list:
        lista_verificar.append(cat.categoria_desc)
    count = 0
    for produto in pedido.produtos:
        if produto.categoria.categoria_desc in lista_verificar:
            index = categoria_list.index(produto.categoria.categoria_desc)
            categoria_list.pop(index)
    
    if count < 7 or not categoria_list:
        return False
    else:
        return True
    

class PedidoViewSet(viewsets.ModelViewSet):
    """
        Pedido incomplete
            view para registro de pedidos e registro de atividades 
            no trello utilizando api Trello
    """
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

    def create(self, request): 
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            pedido = serializer.save()
        else:
            return Response(pedido.errors, status=400)
        
        if not check_pedido_valid(pedido):
            return Response({'detail': 'Produtos não fecham um pedido'}, status=status.HTTP_400_BAD_REQUEST, headers=headers)
        
        create_card(pedido)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
 