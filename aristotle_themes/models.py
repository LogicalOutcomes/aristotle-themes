from django.db import models

DEFAULT_THEME = 'bootstrap-material-design'

THEMES = {
    'bootstrap-material-design': {
        'css_files': [
            'bootstrap-material-design/dist/css/bootstrap-material-design.min.css',
            'bootstrap-material-design/dist/css/ripples.min.css',
        ]
    }
}
