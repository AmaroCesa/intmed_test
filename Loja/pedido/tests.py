from django.test import TestCase

class PedidoTest(TestCase):
    """
        Pedido Incompleto
        Testar Api Registro de pedido;
        Testar Api Mudança de status;
        Testar trello Gerenciamento;
        Testar trello Modificaçoes;

    """
    def test_posso_criar_pedido(self):
        data = {
            'username' : 'teste',
            'password1':'1@345678',
            'password2':'1@345678',
            'email':'test@test.com',
            'telefone' : '878786237',
        }
        
        response = self.client.post(reverse('rest_register'), data=data )
        cliente = Cliente.objets.all().first()
        data = {
            'cliente': cliente.pk,
            'statu_pedido': 'Pedido Realizado',
            'nome': 'Teste',
            'email' : 'test@test.com',
            'telefone' : '898323277',
            'placa_video' : 'Placa de Video',
            'processador' : 'Processador',
            'memoria' : 'memoria',
            'disco' : str(disco),
            'gabinete' : 'gabinete',
            'placa_mae' : 'placa_mae',
            'fonte' : 'fonte',       
        }
        
        response = self.client.post(reverse_lazy('pedido-list'), data=data)
        import ipdb; ipdb.set_trace()