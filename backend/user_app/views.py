import io

import username as username
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.decorators import api_view, renderer_classes, action
from django.shortcuts import render


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class UserModelViewSet(ModelViewSet):
    pagination_class = UserLimitOffsetPagination
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['get'])
    def get_user_name(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return Response({'name': str(user)})

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username:
            return User.objects.filter(username=username)
        return User.objects.all()