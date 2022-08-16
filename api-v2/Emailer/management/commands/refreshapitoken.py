from django.core.management.base import BaseCommand

from Emailer.gmail import get_gmail_service


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_gmail_service()
