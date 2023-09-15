from django import template

register = template.Library()


@register.filter(name='stars')
def stars(value):
    value = int(value)
    return '⭐' * value


register.filter('stars', stars)
