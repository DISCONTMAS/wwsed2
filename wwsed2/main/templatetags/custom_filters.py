# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def format_number(value):
    return '{:,.0f}'.format(value).replace(',', ' ')

@register.filter
def format_date(value):
    return value.strftime('%d %B')

@register.filter
def yes_no(value):
    return 'Да' if value else 'Нет'
