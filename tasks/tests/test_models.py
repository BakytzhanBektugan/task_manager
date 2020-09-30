from django.test import TestCase
from tasks.models import Task, TaskHistory
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='alice',
                                        password='alice12345')

        self.task = Task.objects.create(
            owner=self.user,
            title='Test task',
            description='Test task description',
            status='N'
        )

    def test_task_history(self):
        self.assertEqual(TaskHistory.objects.count(), 1)
