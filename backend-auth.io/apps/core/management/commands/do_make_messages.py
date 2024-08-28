import os

from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.management import call_command
from django.apps import apps


class Command(BaseCommand):
    help = "Command to send strings to rosetta"

    def add_arguments(self, parser):
        parser.add_argument(
            'app_name',
            type=str,
            nargs='?',
            default='all',
        )

    def handle(self, *args, **options):
        app_name = options.get("app_name", "all")
        app_list = (
            settings.INSTALLED_APPS
            if app_name == "all"
            else [f"apps.{app_name}"]
        )
        self._do_send_translations(app_list)

    def _do_send_translations(self, app_list):
        for app in app_list:
            self._show_message(
                f"--> [{app}] Processando ...",
                "WARNING"
            )
            if app in settings.PROJECT_APPS:
                self._create_locale(app)

        self._show_message(
            "--> Gerando arquivos de tradução...\n",
            "WARNING"
        )

        for language in settings.LANGUAGES:
            call_command(
                'makemessages', '-l',
                self._convert_language_code(language[0])
            )

        self._show_message(
            "\n--> Compilando arquivos...",
            "WARNING"
        )
        call_command('compilemessages')
        self._show_message("--> Finalizado!")

    def _create_locale(self, app):
        app_config = apps.get_app_config(app.replace("apps.", ""))
        path = f"{app_config.path}/locale"
        if not os.path.exists(path):
            self._show_message(
                f"--> [{app}] Criando pasta locale...",
                "NOTICE"
            )
            os.makedirs(path)

    def _show_message(self, message, color="SUCCESS"):
        message = getattr(self.style, color)(message)
        self.stdout.write(message)

    def _convert_language_code(self, language):
        parts = language.split('-')
        if len(parts) == 2:
            return f"{parts[0]}_{parts[1].upper()}"
        return language
