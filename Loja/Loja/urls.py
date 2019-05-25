
from django.contrib import admin
from django.urls import path
from django.urls import include 
from .routers import router
from pedido.views import trello_callback 
from estoque.views import EstoqueView
"""
Urls para api cliente
   login / logout : path('rest-auth/', include('rest_auth.urls')),
   register :  path('rest-auth/registration/', include('rest_auth.registration.urls'))
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('estoque/', EstoqueView.as_view(), name='estoque'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('trellocallback', trello_callback),

]
