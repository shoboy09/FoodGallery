from django import template

register = template.Library()


@register.filter
def get_icon_class(icon_classes, key):
    return icon_classes.get(key, 'question-circle')
