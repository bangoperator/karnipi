from django import template

register = template.Library()

@register.filter(name='calc_temp')
def calc_temp(value, arg):
    return int(value) * 100 / int(arg)
