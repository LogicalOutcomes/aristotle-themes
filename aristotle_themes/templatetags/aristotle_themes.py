from django import template
from django.conf import settings
from ..models import THEMES, DEFAULT_THEME

register = template.Library()

config = getattr(settings, 'ARISTOTLE_SETTINGS', {})


@register.assignment_tag
def get_main_scss_file():
    """
    Get main scss file from django settings
    Usage: {% get_main_scss_file as main_scss %}
    """
    return config.get(
        'THEMES_MAIN_SCSS',
        'scss/aristotle_theme.scss'
    )


@register.assignment_tag
def get_theme():
    """
    Get a list of css files to include
    Usage: {% get_theme as theme %}
    """
    theme_name = config.get(
        'THEMES_NAME',
        DEFAULT_THEME
    )
    themes = config.get(
        'THEMES_LIST',
        THEMES,
    )
    if theme_name in themes:
        return themes[theme_name]
    else:
        return {}
