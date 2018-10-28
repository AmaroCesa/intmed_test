from django.test import TestCase
from cliente.models import Cliente
from .models import Produto
from .models import Categoria
from django.urls import reverse_lazy

# Create your tests here.
class ProdutoTest(TestCase):
    def setUp(self):
        user = Cliente.objects.create_superuser(username='teste', password='1@345678', email='test@test.com')
        self.cliente = self.client.force_login(user)
        self.categoria = Categoria.objects.create(categoria_desc='DISCORIGIDO')
    def test_register_poduto(self):
        data = {
            'especificacoes': 'TESTETESTESTESTETSTESTEST',
            'preco':  12.1 ,
            'categoria': self.categoria.id,
        }
        response = self.client.post(reverse_lazy('produto-list'), data=data)
        produto = Produto.objects.all().first()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['especificacoes'], produto.especificacoes)