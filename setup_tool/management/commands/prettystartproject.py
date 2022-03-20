from django.core.checks.security.base import SECRET_KEY_INSECURE_PREFIX
from django.core.management.base import BaseCommand
from django.core.management.templates import TemplateCommand
from django.core.management.commands.startproject import Command as Cmd
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = (
        "Creates a Django project directory structure for the given project "
        "name in the current directory or optionally in the given directory."
    )
    missing_args_message = "You must provide a project name."

    def handle(self, *args, **options):
        project_name = options.pop("name")  # django_project
        target = options.pop("directory")  # .

        # Create a random SECRET_KEY to put it in the main settings.
        options["secret_key"] = SECRET_KEY_INSECURE_PREFIX + get_random_secret_key()

        TemplateCommand().handle("project", project_name, target, **options)