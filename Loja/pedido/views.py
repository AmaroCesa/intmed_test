# from django.shortcuts import render
from django.conf import settings
# Create your views here.
from rest_framework import views

# from django.conf import settings
# from django.dispatch import receiver
# from trello_webhooks.signals import callback_received

# @receiver(callback_received, dispatch_uid="callback_received")
# def on_callback_received(sender, **kwargs):
#     event = kwargs.pop('event')
#     arq = open("log.txt", "w")
#     arq.write(str(event))
#     arq.close
#     print(event)

class PedidoView(views.APIView):
    """
        Pedido incomplete
            view para registro de pedidos e registro de atividades 
            no trello utilizando api Trello
    """

