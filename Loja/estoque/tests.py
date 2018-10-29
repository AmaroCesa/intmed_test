from django.test import TestCase,  Client
from estoque.models import Estoque
from produto.models import Categoria
from produto.models import Produto
from cliente.models import Cliente
from django.urls import reverse_lazy
from django.test import Client
# Create your tests here.
class EstoqueTest(TestCase):
    def setUp(self):
        
        user = Cliente.objects.create_superuser(username='teste', password='1@345678', email='test@test.com')
        self.client = Client()
        self.client.force_login(user)
        self.categoria = Categoria.objects.create(categoria_desc='DISCORIGIDO')
        #Para que o produto inserido no estoque
        data = {
            'especificacoes': 'TESTETESTESTESTETSTESTEST',
            'preco':  12.1 ,
            'categoria': self.categoria.id,
        }
        response = self.client.post(reverse_lazy('produto-list'), data=data)
        self.produto  = Produto.objects.all().first()

    def test_update_estoque(self):
        data ={
            'prodoto_pk': self.produto.id,
            'quantidade_em_estoque' : 10,
            'quantidade_venda' : 5
        }
       
        response = self.client.put(reverse_lazy('estoque'), data=data, content_type='application/json')
        
