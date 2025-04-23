# cars/templatetags/action_buttons.py
from django import template
from django.urls import reverse

register = template.Library()

# Inclusion tag to render the button component
@register.inclusion_tag('cars/_action_button.html')
def action_button(url_name, text, icon=None, variant='primary', type='solid'):
    return {
        'url': reverse(url_name),
        'text': text,
        'icon': icon,
        'variant': variant,
        'type': type
    }

# Template filter to safely map variant|type → class string
@register.filter
def button_classes(variant_type):
    variant, type_ = variant_type.split('|')

    base = "font-bold py-2 px-4 rounded transition-colors flex items-center gap-1"

    # Map combinations
    if type_ == 'solid':
        styles = {
            'primary': 'bg-blue-500 hover:bg-blue-700 text-white',
            'secondary': 'bg-red-500 hover:bg-gray-300 text-gray-800',
            'danger': 'bg-red-500 hover:bg-red-700 text-white',
            'success': 'bg-green-500 hover:bg-green-700 text-white'
        }
    elif type_ == 'outline':
        styles = {
            'primary': 'border border-blue-500 text-blue-500',
            'danger': 'border border-red-500 text-red-500'
        }
    elif type_ == 'ghost':
        styles = {
            'primary': 'bg-transparent text-blue-500',
            'danger': 'bg-transparent text-red-500'
        }
    elif type_ == 'link':
        return f"{base} underline text-blue-500 p-0 bg-transparent"
    elif type_ == 'icon':
        styles = {
            'primary': 'p-2 rounded-full text-white bg-blue-500',
            'danger': 'p-2 rounded-full text-white bg-red-500'
        }
    elif type_ == 'elevated':
        styles = {
            'primary': 'bg-blue-500 text-white shadow-md hover:shadow-lg'
        }
    else:
        return f"{base} bg-gray-300 text-black"

    return f"{base} {styles.get(variant, 'bg-gray-300 text-black')}"
