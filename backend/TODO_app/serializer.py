from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from .models import Project, Task, User
from user_app.serializer import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)
    users = UserModelSerializer
    #users = StringRelatedField(many=True)
    #users = User.username

    class Meta:
        model = Project
        fields = '__all__'


class TaskModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)
    users = UserModelSerializer
    projects = Project.title

    class Meta:
        model = Task
        fields = '__all__'