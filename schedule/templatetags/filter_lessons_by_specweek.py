from django import template
register = template.Library()

@register.filter
def filter_lessons_by_specweek(lessons, i):

    return lessons.filter(spec_week=i)

