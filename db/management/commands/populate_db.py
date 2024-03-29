import os
from django.conf import settings
from django.core.management import BaseCommand
from db.management.commands.populate_peekbank import process_peekbank_dirs

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "Populate Peekbank MySQL Database"

    def add_arguments(self, parser):
        parser.add_argument('--data_root', help='Root directory to add to database')
        
        parser.add_argument('--validate_only', help="Only validate and don't upload to the database", action='store_true')

        parser.add_argument('--dataset', help="Select only a single dataset to process. Pass the name as a string.", type=str, required=False)

    # A command must define handle()
    def handle(self, *args, **options):
        print('Called populate_db with data_root '+options.get('data_root'))
        
        process_peekbank_dirs(options.get('data_root'),
            options.get('validate_only'),
            options.get('dataset'))
