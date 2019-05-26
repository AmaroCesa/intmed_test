from django.test import TestCase

class PedidoTest(TestCase):
    """
        Pedido Incompleto
        Testar Api Registro de pedido;
        Testar Api Mudança de status;
        Testar trello Gerenciamento;
        Testar trello Modificaçoes;

    """
    def test_posso_criar_card(self):
        data ={
            'prodoto_pk': self.produto.id,
            'quantidade_em_estoque' : 10,
            'quantidade_venda' : 5
        }
       
        response = self.client.post(reverse_lazy('pedido-list'), data=data)
