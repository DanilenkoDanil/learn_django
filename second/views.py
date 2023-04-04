from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from second.serializers import UserSerializer 

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [
        permissions.IsAuthenticated   
    ]