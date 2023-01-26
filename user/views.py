from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import CustomUserSerializer

# Create your views here.

class CustomUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer