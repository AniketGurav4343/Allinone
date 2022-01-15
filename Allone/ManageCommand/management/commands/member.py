from os import O_TEMPORARY
from random import choice, choices
from django.core.management.base import BaseCommand, CommandError
from ManageCommand.models import CommandEmployee
class Command(BaseCommand):
    def add_arguments(self, parser):
        # parser.add_argument('id',type=int)
        parser.add_argument('name')
        parser.add_argument('region', choices=['NA','EU'])
        parser.add_argument('--moderator', action='store_true')


    def handle(self, *args, **options):
        employee = CommandEmployee(
            name=options['name'],
            region=options['region'],
            moderator=options['moderator']
        )
        employee.save()
        self.stdout.write('Added member!')


        # employee = CommandEmployee(
        #     id=options['id'], 
        # )
        # employee.delete()
        # self.stdout.write('member delete!')