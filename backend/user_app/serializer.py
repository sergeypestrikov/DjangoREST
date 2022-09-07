from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'add_info', 'email']


class UserModelSerializerV2(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'is_superuser']
