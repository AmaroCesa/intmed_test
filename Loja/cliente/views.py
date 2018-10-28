from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import generics

from rest_framework import serializers
from rest_framework.decorators import list_route
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework import views
from django.contrib.auth import login, authenticate


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    
