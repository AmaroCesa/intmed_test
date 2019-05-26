from rest_framework import routers
from produto.views import ProdutoViewSet
from cliente.views import ClienteViewSet
from cliente.views import PedidoViewSet

router = routers.DefaultRouter()
router.register('produto',ProdutoViewSet, base_name='produto')
router.register('cliente',ClienteViewSet, base_name='cliente')
router.register('pedido',PedidoViewSet, base_name='pedido')