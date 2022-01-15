from django.core.management.base import BaseCommand, CommandError
class Command(BaseCommand):

    help='The help information for this Command.'

    # def add_arguments(self, parser): #use to declear objects
    #     parser.add_argument('first')
    #     parser.add_argument('--option1')

    # def handle(self, *args, **options): #use to create method
    #     print("Command:Mycommand")
    #     print(f'first:{options["first"]}')
    #     print(f'Option1:{options["option1"]}')

# py .\manage.py mycommand "first send and" --option1 someting

    def add_arguments(self, parser):
        parser.add_argument('first', type=int, help='A number less than 100')
        parser.add_argument('second', nargs=3, type=str, help='Three strings.')
        parser.add_argument('--option1', default='anything', help="The option Value")
        parser.add_argument('--option2', action='store_true', help="True is passed")

    def handle(self, *args, **options):
        if options['first']<100:
            self.stdout.write('GOOD JOB. The  number is less than 100')
        else:
            raise CommandError('That number is grather than 100')


        for values in options['second']:
            self.stdout.write(f'values :{values}')


        self.stdout.write(f'The value for --option1 is {options["option1"]}')
        
        if options['option2']:
            self.stdout.write('Option2 is TRUE')
        else:
            self.stdout.write('Option2 is FALSE')

