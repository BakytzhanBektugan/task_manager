from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from ..views import TaskViewSet
from ..models import Task
from rest_framework.authtoken.models import Token


class TestViews(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='alice',
                                        password='alice12345')

        self.user2 = User.objects.create(username='bob',
                                        password='bob12345')

        self.data = {
            'owner': self.user,
            'title': 'Task 1',
            'description': 'Task 1 description',
            'status': 'N'
        }

        self.data2 = {
            'title': 'Changed task',
            'status': 'P'
        }

        self.task = Task.objects.create(
            owner=self.user,
            title='Test task',
            description='Test task description',
            status='N'
        )

        self.token = Token.objects.create(user=self.user)
        self.token2 = Token.objects.create(user=self.user2)

    def test_task_viewset_unauthorized_get(self):
        factory = APIRequestFactory()
        view = TaskViewSet.as_view(actions={'get': 'list'})
        response = view(factory.get(reverse('tasks_list')))
        self.assertEqual(response.status_code, 401)

    def test_task_viewset_authorized_get(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
        response = self.client.get(reverse('tasks_list'))
        self.assertEqual(response.status_code, 200)

    def test_task_viewset_authorized_access_another_person_data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token2))
        response = self.client.get(reverse('tasks_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_task_viewset_authorized_post(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
        response = self.client.post(reverse('tasks_list'), self.data)
        self.assertEqual(response.status_code, 201)

    def test_task_viewset_authorized_patch(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
        response = self.client.patch(reverse('task_detail', kwargs={'pk': self.task.id}), self.data2)
        self.assertIn(response.status_code, [200, 204])

    def test_taskhistory_list_unauthorized_get(self):
        response = self.client.get(reverse('task_history', kwargs={'pk': self.task.id}))
        self.assertEqual(response.status_code, 401)

    def test_taskhistory_list_authorized_get(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
        response = self.client.get(reverse('task_history', kwargs={'pk': self.task.id}))
        self.assertEqual(response.status_code, 200)