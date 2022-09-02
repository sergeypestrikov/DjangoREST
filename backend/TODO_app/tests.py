from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from .views import ProjectModelViewSet
from .models import Project
from mixer.backend.django import mixer


class ProjectClientTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.project = Project.objects.create(title='Спасти мир')

    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post(self):
        self.client.login(username='sergey', password='12345')
        response = self.client.post('/api/projects/', {
            "id": 2,
            "title": "Take over the world",
            "repo": null,
            "users": [
                5
            ]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(pk=response.get('id'))
        self.assertEqual(project.title, 'Take over the world')
