from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectModelViewSet, TaskModelViewSet

app_name = 'TODO_app'

router = DefaultRouter()
# router = SimpleRouter()
router.register('projects', ProjectModelViewSet)
router.register('tasks', TaskModelViewSet)


urlpatterns = [
    path('', include(router.urls))
]