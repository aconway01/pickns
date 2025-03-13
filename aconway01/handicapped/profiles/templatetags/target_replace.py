from django import template

register = template.Library()


@register.filter
def target_replace(value):
    return value.replace('a href', 'a target="_blank" href')
