from django import template
from django.conf import settings

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
