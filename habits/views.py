from django.db.models import Q
from rest_framework import generics

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwnerOrReadOnly, CanViewPublicHabits
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrReadOnly]


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [CanViewPublicHabits]
    pagination_class = HabitsPaginator


    def get_queryset(self):
        # Возвращаем только привычки пользователя и публичные привычки
        if self.request.user.is_authenticated:  # Проверяем, аутентифицирован ли пользователь
            return Habit.objects.filter(Q(user=self.request.user) | Q(is_public=True))
        else:
            return Habit.objects.filter(is_public=True)  # Если пользователь не аутентифицирован, возвращаем только публичные привычки

    # def get_queryset(self):
    #     # Возвращаем только привычки пользователя и публичные привычки
    #     return Habit.objects.filter(Q(user=self.request.user) | Q(is_public=True))


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
