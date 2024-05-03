from django import template

register = template.Library()


@register.filter(name='custom_enumeration')
def custom_enumeration(value):
    print(value)
    return "{:02}".format(value)


@register.filter(name='split')
def split(value, arg):
    return value.strip().split(arg)
