from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class UserCreateAPIViewTest(APITestCase):

    def test_create_user(self):
        """ Test Create User """
        data = {
            "email": "test@mail.com",
            "password": "test_password",
            "chat_id": "123445455"
            # Добавьте другие поля, необходимые для создания пользователя
        }
        response = self.client.post(
            reverse('users:user-create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.json())
