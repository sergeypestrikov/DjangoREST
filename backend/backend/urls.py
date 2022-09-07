"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from user_app.views import UserModelViewSet
from TODO_app.views import *
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, License, Contact

schema_view = get_schema_view(
    Info(
        title='Library',
        default_version='1.0',
        description='Description',
        license=License(name='MIT'),
        contact=Contact(email='mail@mail.ru')
    )
)


router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('tasks', TaskModelViewSet)
router.register('projects', ProjectModelLimitedViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/', include('user_app.urls')),
    # path('api/2.0/', include(router.urls, namespace='2.0')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', views.obtain_auth_token),
    # path('api/<str:version>/users', UserModelViewSet.as_view({'get': 'list'})),
    # path('api/<str:version>/projects', ProjectModelViewSet.as_view({'get': 'list'})),
    # path('api/<str:version>/tasks', TaskModelViewSet.as_view({'get': 'list'})),
    path('project_get', project_get),
    path('project_api_get', project_api_get),
    path('project_api_get_class', ProjectApiView.as_view()),
    path('project_api_get_list', ProjectListAPIView.as_view()),
    path('swagger', schema_view.with_ui()),
    # re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
]