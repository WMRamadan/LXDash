from django import template

register = template.Library()

@register.filter
def get_key(value, arg):
    return value.get(arg, None)

@register.filter
def get_value(dict_name, key_name):
    return dict_name.get(key_name, '')

register.filter('get_key', get_key)
register.filter('get_value', get_value)
