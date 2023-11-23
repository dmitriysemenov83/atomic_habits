from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitList

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit-list'),
    path('public/', PublicHabitList.as_view(), name='public'),
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('retrieve/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-retrieve'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
]
