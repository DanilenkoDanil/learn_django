from django.shortcuts import render
from steam.models import Mail, Game, Account
from rest_framework import viewsets, permissions
from steam.serializers import AccountSerializer 

# Create your views here.

class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permissions_classes = [
        permissions.IsAuthenticated   
    ]