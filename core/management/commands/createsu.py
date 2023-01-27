from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='Admin').exists():
            User.objects.create_superuser(
                username=os.environ('DB_USER'),
                email=os.environ('DB_EMAIL'),
                password=os.environ('DB_PASSWORD')
            )
        print('Superuser has been created.')
