from django.conf import settings
from trello import TrelloClient
from pedido.models import Pedido
from cliente.models import Cliente
from django.template import loader

def get_component(pedido, categoria):
    for produto in pedido.produtos.all():
        return produto.especificacoes if (produto.categoria.categoria_desc == categoria) else None

def check_board(boards):
        for board in boards:
            if board.name == settings.BOARD_NAME:
                return board

def create_card(pedido):    
    cliente = pedido.cliente
    placa_video = get_component(pedido, 'Placa de Vídeo')
    processador = get_component(pedido, 'Processadores')
    memoria = get_component(pedido, 'Memória RAM')
    disco = get_component(pedido, 'Disco Rígido/SSD')
    gabinete = get_component(pedido, 'Gabinete')
    placa_mae = get_component(pedido, 'Placa mãe')
    fonte = get_component(pedido, 'Fonte')
    data = {
        'statu_pedido': str(pedido.statu_pedido),
        'username': str(cliente.username),
        'email' : str(cliente.email),
        'telefone' : str(cliente.telefone),
        'placa_video' : str(placa_video),
        'processador' : str(processador),
        'memoria' : str(memoria),
        'disco' : str(disco),
        'gabinete' : str(gabinete),
        'placa_mae' : str(placa_mae),
        'fonte' : str(fonte),
        }
    client = TrelloClient(api_key=settings.API_KEY,  token=settings.TRELLO_API_SECRET)
    if settings.BOARD_NAME:
        board = check_board(client.list_boards())
        if client.list_hooks() == []:
            client.create_hook(settings.CALLBACK_DOMAIN, board.id)
        for lista in board.all_lists():
            if lista.name == pedido.statu_pedido:
                lista.add_card(name=f'Pedido {pedido.id}', desc=loader.render_to_string('pedido_template.txt', data))
