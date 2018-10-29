from django.shortcuts import render
from django.conf import settings
# Create your views here.
from rest_framework import views

class PedidoView(views.APIView):
    """
        Pedido incomplete
            view para registro de pedidos e registro de atividades 
            no trello utilizando api Trello
    """