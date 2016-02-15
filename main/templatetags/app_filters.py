from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter(name='calc_temp')
def calc_temp(value, arg):
    return value * 100 / arg