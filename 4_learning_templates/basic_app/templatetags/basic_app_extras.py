from django import template

register = template.Library()

@register.filter(name='string_cut')
def string_cut(value, arg):
    """
    This cuts out all balues of 'arg' from the string!
    """
    return value.replace(arg, '')

# You would use the following if you don't want to use decorators : register.filter('string_cut', string_cut)