from rest_framework import routers
from produto.views import ProdutoViewSet
from cliente.views import ClienteViewSet

router = routers.DefaultRouter()
router.register('produto',ProdutoViewSet, base_name='produto')
router.register('cliente',ClienteViewSet, base_name='cliente')