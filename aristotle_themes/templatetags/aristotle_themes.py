from django import template
from django.conf import settings
from ..models import THEMES, DEFAULT_THEME

register = template.Library()


@register.assignment_tag
def get_main_scss_file():
    """
    Get main scss file from django settings
    Usage: {% get_main_scss_file as main_scss %}
    """
    return getattr(
        settings,
        'ARISTOTLE_THEMES_SCSS',
        'scss/aristotle_theme.scss'
    )


@register.assignment_tag
def get_themes_css_files():
    """
    Get a list of css files to include
    Usage: {% get_themes_css_files as css_files %}
    """
    theme_name = getattr(
        settings,
        'ARISTOTLE_THEMES_NAME',
        DEFAULT_THEME
    )
    if theme_name in THEMES:
        return THEMES[theme_name]['css_files']
    else:
        return []
