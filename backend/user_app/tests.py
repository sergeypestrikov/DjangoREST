from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase, APIClient
from .views import UserModelViewSet
from .models import User
from django.contrib.auth.models import User
from mixer.backend.django import mixer


class UserTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='sergey', password='12345')
        self.user = mixer.blend(User)

    def tearDown(self) -> None:
        pass

    def test_get_list_1(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_2(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        force_authenticate(request, user=self.user)
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ProjectClientTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(username='Leo', name='Leonardo', add_info='Good guy')

    def test_get_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post(self):
        self.client.login(username='sergey', password='12345')
        response = self.client.post('/api/users/', {
            "id": 1,
            "username": "Leo",
            "name": "Leonardo",
            "add_info": "Good guy",
            "email": "leonardo@turtle.com"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(pk=response.get('id'))
        self.assertEqual(user.name, 'Leonardo')