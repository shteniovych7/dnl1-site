from django.shortcuts import render
from .models import ClassSchedule, WEEKDAYS

def schedule(request):
    classes = ClassSchedule.objects.all()
    try:
        class_to_show_id = request.GET.get('class')
        class_to_show = ClassSchedule.objects.get(id=class_to_show_id)

        class_schedule = [
            class_to_show.classlesson_set.filter(day=x[0]) for x in WEEKDAYS
        ]
    except:
        class_schedule = None
    return render(request, 'schedule/schedule.html', {'all_classes': classes,  'class_schedule' : class_schedule, 'range' : range(1, 8), 'class_to_show_id':class_to_show_id})
