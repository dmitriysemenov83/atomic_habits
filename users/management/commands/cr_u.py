from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='user2@example.com',
            first_name='User2',
            last_name='Userov',
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

        user.set_password('qazwsx2020g2')
        user.save()