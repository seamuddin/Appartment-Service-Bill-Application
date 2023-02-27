from django.core.management.commands.runserver import Command as BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run the development server and populate custom permissions'

    def handle(self, *args, **options):
        # Call the populate_permissions command
        call_command('populate_permissions')

        # Call the runserver command
        super().handle(*args, **options)