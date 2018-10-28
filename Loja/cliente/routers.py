from rest_framework import routers
from cliente.views import ClienteViewSet

router = routers.DefaultRouter()
router.register('cliente',ClienteViewSet, base_name='cliente')