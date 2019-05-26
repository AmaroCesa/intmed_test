# from django.shortcuts import render
from django.conf import settings
# Create your views here.
from rest_framework import viewsets
from .trello import create_card
from .serializer import PedidoSerializer
from .models import Pedido
from rest_framework import status
from rest_framework.response import Response

# @receiver(callback_received, dispatch_uid="callback_received")
# def on_callback_received(sender, **kwargs):
#     event = kwargs.pop('event')
#     arq = open("log.txt", "w")
#     arq.write(str(event))
#     arq.close
#     print(event)

def trello_callback(request, *args, **kwargs):
    # arq = open("log.txt", "w")
    # arq.write(request.content)
    # arq.close
    # print(event)
    return Response('', status=200)

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
 