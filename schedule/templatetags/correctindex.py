from django import template
register = template.Library()

@register.filter
def correctindex(indexable, i):
    return i < len(indexable)