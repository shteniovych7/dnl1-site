from django import template
register = template.Library()

@register.filter
def filter_lessons(lessons, i):
    return lessons.filter(index=i)
