import io

from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import Project, Task
from .serializer import ProjectModelSerializer, TaskModelSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from django.shortcuts import render


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    pagination_class = ProjectLimitOffsetPagination
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()

    @action(detail=True, methods=['get'])
    def get_project_name(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        return Response({'id': str(project)})

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        if id:
            return Project.objects.filter(id=id)
        return Project.objects.all()


class TaskLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TaskModelViewSet(ModelViewSet):
    pagination_class = TaskLimitOffsetPagination
    serializer_class = TaskModelSerializer
    queryset = Task.objects.all()


class ProjectModelLimitedViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    serializer_class = TaskModelSerializer
    queryset = Task.objects.all()


class ProjectApiView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def project_api_get(request):
    projects = Project.objects.all()
    serializer = ProjectModelSerializer(projects, many=True)
    return Response(serializer.data)


def project_get(request):
    projects = Project.objects.all()
    serializer = ProjectModelSerializer(projects, many=True)