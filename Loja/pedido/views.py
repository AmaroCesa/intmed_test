# from django.shortcuts import render
from django.conf import settings
# Create your views here.
from rest_framework import viewsets
from .trello import create_card
from .serializer import PedidoSerializer

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
    arq = open("log.txt", "w")
    arq.write(request.content)
    arq.close
    print(event)

class PedidoViewSet(viewsets.ModelViewSet):
    """
        Pedido incomplete
            view para registro de pedidos e registro de atividades 
            no trello utilizando api Trello
    """
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

    def create(self, request): 
        try:
            card = super(PedidoViewSet, self).create(request)
        except Exception as e:
            return  Response(e, status=status.HTTP_400_BAD_REQUEST, headers=headers)
        if card =={}:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            headers = serializer.data
            create_card(headers)
        return card 