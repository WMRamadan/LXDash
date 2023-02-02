from django import template

register = template.Library()

@register.filter
def get_value(dict_name, key_name):
    return dict_name.get(key_name, '')

register.filter('get_value', get_value)
