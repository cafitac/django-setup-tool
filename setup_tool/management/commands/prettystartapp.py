from django.core.management import BaseCommand
from django.core.management.templates import TemplateCommand


class Command(BaseCommand):
    help = (
        "Creates a Django app directory structure for the given app name in "
        "the current directory or optionally in the given directory."
    )
    missing_args_message = "You must provide an application name."

    def handle(self, **options):
        app_name = options.pop("name")
        target = options.pop("directory")

        options["template"] = './setup_tool/app_template'

        TemplateCommand().handle("app", app_name, target, **options)
