from django.db import models

from users.models import User, NULLABLE


class Habit(models.Model):
    PERIOD = (
        ('DAILY', 'каждый день'),
        ('WEEKLY', 'раз в неделю')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    place = models.CharField(max_length=255, verbose_name='Место')
    time = models.TimeField(verbose_name='Время', **NULLABLE)
    action = models.CharField(max_length=255, verbose_name='Действие')
    is_pleasant = models.BooleanField(verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='Связанная привычка')
    period = models.CharField(max_length=10, choices=PERIOD, default='DAILY', verbose_name='Периодичность')
    reward = models.CharField(max_length=255, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='Время на выполнение в секундах', default=2)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
