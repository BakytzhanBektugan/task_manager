from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class AuthViewTests(APITestCase):

    def setUp(self):
        self.data = {
            'username': 'bob',
            'password': 'bob12345'
        }
        self.user = User.objects.create(username='alice',
                                        password='alice12345')
        self.token = Token.objects.create(user=self.user)

    def test_user_registration(self):
        response = self.client.post('/auth/users/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))
        response = self.client.get('/auth/users/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
