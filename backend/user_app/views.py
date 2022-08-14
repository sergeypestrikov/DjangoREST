from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserModelSerializer
from django.shortcuts import render


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

