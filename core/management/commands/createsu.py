from core.user.models import User
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='Admin').exists():
            User.objects.create_superuser(
                username=os.getenv('DB_USER'),
                email=os.getenv('DB_EMAIL'),
                password=os.getenv('DB_PASSWORD')
            )
        print('Superuser has been created.')
