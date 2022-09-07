import io

import username as username
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserModelSerializer, UserModelSerializerV2
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.decorators import api_view, renderer_classes, action
from django.shortcuts import render


class CustomPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.username == 'sergey'

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)

    # def has_permission(self, request, view):
    #     return request.user and request.user.name == 'sergey'


# class UserLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 10


class UserModelViewSet(ModelViewSet):
    # pagination_class = UserLimitOffsetPagination
    # permission_classes = [IsAuthenticated]
    # permission_classes = [DjangoModelPermissions]
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserModelSerializerV2
        return UserModelSerializer

    @action(detail=True, methods=['get'])
    def get_user_name(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return Response({'name': str(user)})

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username:
            return User.objects.filter(username=username)
        return User.objects.all()