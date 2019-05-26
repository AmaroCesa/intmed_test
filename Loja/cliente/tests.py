from django.test import TestCase
from django.urls import reverse_lazy
from django.urls import reverse
from cliente.models import Cliente
# Create your tests here.
class TestCliente(TestCase):
    def test_register_cliente(self):
        """
            testar registro de cliente atraves da API Rest
        """
    
        data = {
            'username' : 'teste',
            'password1':'1@345678',
            'password2':'1@345678',
            'email':'test@test.com',
            'telefone' : '878786237',
        }
        
        response = self.client.post(reverse('rest_register'), data=data )
        cliente = Cliente.objects.all().first()
        self.assertEqual(cliente.username, 'teste')
        self.assertEqual(response.status_code, 201)
    
    def test_login_logout_cliente(self):
        """
            testar login/logout de cliente atraves da API Rest
        """
        data = {
            'username' : 'teste',
            'password1':'1@345678',
            'password2':'1@345678',
            'email':'test@test.com',
            'telefone' : '878786237',
        }
        response = self.client.post(reverse('rest_register'), data=data )
     
        data_login = {
           'username': 'teste',
           'password': '1@345678'
        }
        response = self.client.post(reverse('rest_login'), data=data_login )
        self.assertEqual(response.status_code, 200)
        
        response = self.client.post(reverse('rest_logout'), data=data_login )
        self.assertEqual(response.status_code, 200)
        