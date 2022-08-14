from rest_framework.viewsets import ModelViewSet
from .models import Project, Task
from .serializer import ProjectModelSerializer, TaskModelSerializer
from django.shortcuts import render


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()


class TaskModelViewSet(ModelViewSet):
    serializer_class = TaskModelSerializer
    queryset = Task.objects.all()
