from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = "Loads ansible modules and builds category tree"

    def handle(self, *args, **kwargs):
        try:
            call_command('load_ansible_modules')
        except CommandError as error:
            print "Error: %s" % (error,)
        try:
            call_command('build_module_categories')
        except CommandError as error:
            print "Error: %s" % (error, )
