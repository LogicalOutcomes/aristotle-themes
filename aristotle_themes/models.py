from django.db import models

DEFAULT_THEME = 'bootstrap-material-design'

THEMES = {
    'bootstrap-material-design': {
        'css_files': [
            'node_modules/bootstrap-material-design/dist/css/bootstrap-material-design.min.css',
            'node_modules/bootstrap-material-design/dist/css/ripples.min.css',
        ],
        'js_files': [
            'node_modules/bootstrap-material-design/dist/js/material.min.js',
            'node_modules/bootstrap-material-design/dist/js/ripples.min.js',
        ]
    }
}
