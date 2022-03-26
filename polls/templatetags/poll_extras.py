from django import template
from jalali_date import date2jalali




register = template.Library()


@register.filter(name='cut')
def cut(value , arg):
    return value.replace(arg , '')


@register.filter(name='show_jalali_date')
def show_jalali_date(value):
    return date2jalali(g_date=value)