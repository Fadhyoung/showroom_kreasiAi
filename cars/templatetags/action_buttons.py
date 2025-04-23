from django import template
from django.urls import reverse

register = template.Library()

@register.inclusion_tag('cars/_action_button.html')
def action_button(url_name, text, icon=None, variant='primary', size='medium', icon_position='left'):
    # Pass the parameters to the template, no need for style handling here
    return {
        'url': reverse(url_name),
        'text': text,
        'icon': icon,
        'variant': variant,
        'size': size,
        'icon_position': icon_position
    }
