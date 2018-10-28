
from django.urls import path
from django.urls import include 
from .routers import router

urlpatterns = [
    path('', include(router.urls))
]
