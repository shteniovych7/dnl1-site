from django import template
register = template.Library()

@register.filter
def filter_lessons_by_subgroup(lessons, i):
    try:
        res = lessons.get(subgroup=i)
    except:
        res = None
    return res
