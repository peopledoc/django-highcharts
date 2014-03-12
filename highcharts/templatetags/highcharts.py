from django.conf import settings
from django import template

register = template.Library()

# Default settings
HIGHCHARTS_DEFAULTS = {
    'jquery_url': '//code.jquery.com/jquery.min.js',
    'highcharts_url': 'http://code.highcharts.com/highcharts.js',
}

# Start with a copy of default settings
HIGHCHARTS = HIGHCHARTS_DEFAULTS.copy()

# Override with user settings from settings.py
HIGHCHARTS.update(getattr(settings, 'HIGHCHARTS', {}))


@register.simple_tag
def highcharts_javascript():
    """
    Return HTML for Bootstrap JavaScript
    """
    javascript = ''
    if HIGHCHARTS['jquery_url']:
        javascript += '<script src="{url}"></script>'.format(url=HIGHCHARTS['jquery_url'])
    if HIGHCHARTS['highcharts_url']:
        javascript += '<script src="{url}"></script>'.format(url=HIGHCHARTS['highcharts_url'])
    return javascript
