import datetime
from celery import shared_task
from habits.models import Habit

from habits.services import habit_massage, send_tg


@shared_task
def mailing_telegram():
    """
        Главная функция рассылки в телеграм бот
    """
    habits = Habit.objects.filter(is_pleasant=False)
    for habit in habits:
        if not habit.is_pleasant:
            time_begin_habit = habit.time
            time_up = datetime.datetime.now() + datetime.timedelta(minutes=5)

            print(time_up.hour, time_up.minute)
            print(time_begin_habit.hour, time_begin_habit.minute)

            if time_up.hour == time_begin_habit.hour and time_up.minute == time_begin_habit.minute:
                # Проверка на совпадение поля date с текущей датой
                if habit.date == datetime.datetime.now().date():
                    user_id = habit.user.chat_id
                    message = habit_massage(habit)
                    send_tg(user_id, message)

                    # Обновление поля date в зависимости от значения поля period
                    habit.date += datetime.timedelta(days=habit.period)
                    habit.save()
