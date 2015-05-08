from django.template import Library

register = Library()

@register.filter
def is_false(value):
    return not value