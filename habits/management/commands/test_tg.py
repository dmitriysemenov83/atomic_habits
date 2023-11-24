from django.core.management import BaseCommand

from config.settings import USER_TG_ID
from habits.services import send_tg

user_id = USER_TG_ID
message = 'проверка рассылки'


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_tg(user_id, message)
