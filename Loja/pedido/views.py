import json
# from django.shortcuts import render
from django.conf import settings
# Create your views here.
from rest_framework import viewsets
from .trello import create_card
from .serializer import PedidoSerializer
from .models import Pedido
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def trello_callback(request, *args, **kwargs):
    #TODO: tratar status pedido verificando mensagem callback
    jsondata = request.body
    data = json.loads(jsondata)
    action = data['action']['data']
    if action or action != {}:
        pedido_id = action['card']['name'].split(' ')[1]
        
        pedido = Pedido.objects.filter(pk=pedido_id).first()
        print('####################', pedido)
        status = action['listAfter']['name']
        pedido.statu_pedido = status
        print('####################', status)

        pedido.save()
    return HttpResponse(status=200)


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
        create_card(pedido)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
 