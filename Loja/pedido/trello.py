from django.conf import settings
from trello import TrelloClient
from pedido.models import Pedido
from cliente.models import Cliente
from django.template import loader

def create_card(pedido):    
    cliente = pedido.cliente
    # placa_video
    # processador
    # memoria
    # disco
    # gabinete
    # placa_mae
    # fonte
    data = {
        'statu_pedido': str(pedido.statu_pedido),
        'nome': str(cliente.username),
        'email' : str(cliente.email),
        'telefone' : str(cliente.telefone),
        # 'placa_video' : str(pedido.placa_video),
        # 'processador' : str(processador),
        # 'memoria' : str(memoria),
        # 'disco' : str(disco),
        # 'gabinete' : str(gabinete),
        # 'placa_mae' : str(placa_mae),
        # 'fonte' : str(fonte),       
    }
    client = TrelloClient(api_key=settings.API_KEY,  token=settings.TRELLO_API_SECRET)
    if settings.BOARD_NAME:
        board = check_board(client.lsit_boards())
       
        for lista in board.all_lists():
            if lista.name == pedido.statu_pedido:

                lista.add_card(name=f'Pedido {pedido.id}', desc=loader.render_to_string('pedido_template.txt', data))

    add_card(self, name, desc=None)

def check_board(boards):
        for board in boards:
            if board.name == settings.BOARD_NAME:
                return board