from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from .models import Project, Task
from user_app.serializer import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TaskModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)
    projects = Project.title

    class Meta:
        model = Task
        fields = '__all__'