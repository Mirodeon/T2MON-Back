from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                email=os.getenv('DB_EMAIL')
            )
        print('Superuser has been created.')
