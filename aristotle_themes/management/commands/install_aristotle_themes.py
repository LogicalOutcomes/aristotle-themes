from __future__ import unicode_literals
import os
import subprocess
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populate static data for Aristotle Themes'

    def handle(self, *args, **options):
        module_path = os.path.dirname(__file__)
        self.local_path = os.path.join(module_path, '../../')
        self.static_path = os.path.join(self.local_path, 'static')
        self.modules_path = os.path.join(self.static_path, 'node_modules')

        self.stdout.write('Collecting npm dependencies')
        self.npm_install(self.static_path)
        self.stdout.write('Aristotle theme is ready. Please run collectstatic now.')

    def npm_install(self, path=None):
        npm_executable_path = getattr(settings, 'NPM_EXECUTABLE_PATH', 'npm')
        command = [
            npm_executable_path,
            'install',
            '--prefix=' + path
        ]

        proc = subprocess.Popen(
            command,
            env={'PATH': os.environ.get('PATH')},
        )
        proc.wait()
