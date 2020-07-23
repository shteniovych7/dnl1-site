from django.shortcuts import render

from teachers.models import Teacher

from .models import ClassSchedule, WEEKDAYS


def schedule(request):
    classes = ClassSchedule.objects.all()
    teachers = Teacher.objects.all()
    class_to_show_id = teacher_to_show_id = class_schedule = None

    schedule_type = request.GET.get('type')
    if schedule_type == 'students_schedule':
        class_to_show_id = request.GET.get('class')
        class_to_show = ClassSchedule.objects.get(id=class_to_show_id)

        class_schedule = [
            class_to_show.lessons.filter(day=x[0]) for x in WEEKDAYS
        ]
    elif schedule_type == 'teachers_schedule':
        teacher_to_show_id = request.GET.get('teacher')
        teacher_to_show = Teacher.objects.get(id=teacher_to_show_id)

        class_schedule = [
            teacher_to_show.teacher_lessons.filter(day=x[0]) for x in WEEKDAYS
        ]

    args = {
        'schedule_type': schedule_type,
        'all_classes': classes,
        'all_teachers': teachers,
        'class_to_show_id': class_to_show_id,
        'teacher_to_show_id': teacher_to_show_id,
        'class_schedule': class_schedule,
        'range': range(1, 9),
        'weekdays': WEEKDAYS,
    }

    temp = 'schedule/schedule.html'

    day = request.GET.get('day', '')
    if day:
        temp = 'schedule/mobile_view.html'
        week = [x[0] for x in WEEKDAYS ]
        args['day_index'] = week.index(day)

    return render(request, temp, args)
