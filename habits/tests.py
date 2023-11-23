from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.com', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place='Тест',
            time='20:38:39',
            date='2023-11-22',
            action='Тест',
            is_pleasant=True,
            period=1,
            time_to_complete=120,
        )

    def test_get_habit(self):
        """ Test Habits List """

        response = self.client.get(
            reverse('habits:habit-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        print(response.json())

    def test_create_habit(self):
        """ Test Create habit """
        self.client.force_authenticate(user=self.user)
        data = {
            "place": "Create Test",
            "time": self.habit.time,
            "date": self.habit.date,
            "action": "Test",
            "is_pleasant": self.habit.is_pleasant,
            "period": self.habit.period,
            "time_to_complete": self.habit.time_to_complete
        }
        response = self.client.post(
            reverse('habits:habit-create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.json())

    def test_update_habit(self):
        """ Test Update habit """
        data = {
            "place": "Update Test",
            "time": self.habit.time,
            "date": self.habit.date,
            "action": "Test",
            "is_pleasant": self.habit.is_pleasant,
            "period": self.habit.period,
            "time_to_complete": self.habit.time_to_complete
        }
        response = self.client.put(
            reverse('habits:habit-update', kwargs={'pk': self.habit.id}),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        """ Test Delete Habit """
        response = self.client.delete(
            reverse('habits:habit-delete', kwargs={'pk': self.habit.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_habit(self):
        """ Test Retrieve habit """
        response = self.client.get(
            reverse('habits:habit-retrieve', kwargs={'pk': self.habit.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_public_habits(self):
        """ Test Public Habit List """
        response = self.client.get(
            reverse('habits:public')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
