
from django.contrib import admin
from django.urls import path
from django.urls import include 
# from .routers import router
"""
Urls para api cliente
   login / logout : path('rest-auth/', include('rest_auth.urls')),
   register :  path('rest-auth/registration/', include('rest_auth.registration.urls'))
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cliente.urls')),
    path('api/', include('produto.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
