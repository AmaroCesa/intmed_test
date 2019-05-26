from django.test import TestCase
from cliente.models import Cliente
from produto.models import Produto
from produto.models import Categoria

from django.urls import reverse_lazy


class PedidoTest(TestCase):
    """
        Pedido Incompleto
        Testar Api Registro de pedido;
        Testar Api Mudança de status;
        Testar trello Gerenciamento;
        Testar trello Modificaçoes;

    """
    
    def setUp(self):
        user = Cliente.objects.create_superuser(username='teste', password='1@345678', email='test@test.com')
        self.cliente = self.client.force_login(user)
        self.categoria = Categoria.objects.create(categoria_desc='DISCORIGIDO')
        produto = {
            'especificacoes': 'TESTETESTESTESTETSTESTEST',
            'preco':  12.1 ,
            'categoria': self.categoria.id,
        }
        response = self.client.post(reverse_lazy('produto-list'), data=produto)
        self.produto = Produto.objects.all().first()
        cliente = {
            'username' : 'teste',
            'password1':'1@345678',
            'password2':'1@345678',
            'email':'test@test.com',
            'telefone' : '878786237',
        }
        
        response = self.client.post(reverse('rest_register'), data=cliente )
        self.cliente = Cliente.objets.all().first()

    def test_posso_criar_pedido(self):
        
        data = {
            'cliente': self.cliente.pk,
            'statu_pedido': 'Pedido Realizado',
            'produto': self.produto.pk,       
        }
        
        import ipdb; ipdb.set_trace()
        response = self.client.post(reverse_lazy('pedido-list'), data=data)
        import ipdb; ipdb.set_trace()
