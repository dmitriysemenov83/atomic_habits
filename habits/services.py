import requests
from config.settings import TG_TOKEN


def send_tg(user_id, message):
    """
        Функция для отправки уведомлений в телеграм бот
    """

    token = TG_TOKEN
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': user_id,
        'text': message
    }
    requests.post(url, data=data)


def habit_massage(obj):
    """
        Функция генерации сообщения рассылки
    """
    place = obj.place
    time = obj.time
    action = obj.action
    time_to_complete = obj.time_to_complete
    reward = obj.reward
    related_habit = obj.related_habit
    if reward:
        if time_to_complete:
            return (f"Готовься {action} {place} в {time}, в течении {time_to_complete} секунд,\n"
                    f" после чего можешь {reward}")
        else:
            return f"Готовься {action} {place} в {time}, после чего можешь {reward}"
    elif related_habit:
        if time_to_complete:
            return (f"Готовься {action} {place} в {time}, в течении {time_to_complete} секунд,\n"
                    f" после чего можешь {related_habit.action}")
        else:
            return f"Готовься {action} {place} в {time}, после чего можешь {related_habit.action}"
    else:
        return f"Готовься {action} {place} в {time}. Время на выполнение {time_to_complete} секунд."
