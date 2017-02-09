import os
import subprocess

from django.conf import settings
from npm.finders import NpmFinder, get_npm_root_path


def npm_install(path=None):
    path = os.environ.get('PATH') if not path else path
    npm_executable_path = getattr(settings, 'NPM_EXECUTABLE_PATH', 'npm')
    command = [npm_executable_path, 'install', '--prefix=' + get_npm_root_path()]
    proc = subprocess.Popen(
        command,
        env={'PATH': path},
    )
    proc.wait()


class AirstotleThemesNpmFinder(NpmFinder):
    def __init__(self, *args, **kwargs):
        npm_install(self.__file__)
        super(AirstotleThemesNpmFinder, self).__init__(*args, **kwargs)
