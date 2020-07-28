from django.db import models
from teachers.models import Lesson as LessonList, Teacher
import datetime

class ClassScheduleManager(models.Manager):
    def in_class_growing_order(self, *args, **kwargs):
        qs = self.get_queryset().filter(*args, **kwargs)
        return sorted(qs, key=lambda n: (int(n.class_title.split('-')[0]), n.class_title.split('-')[1]))

class ClassSchedule(models.Model):
    class_title = models.CharField('Клас', max_length=5)

    objects = ClassScheduleManager()

    def __str__(self):
        return self.class_title

    class Meta:
        verbose_name = 'Розклад класу'
        verbose_name_plural = 'Розклади класів'


WEEKDAYS = (
        ('Mo', 'Понеділок'),
        ('Tu', 'Вівторок'),
        ('We', 'Середа'),
        ('Th', 'Четвер'),
        ('Fr', 'П\'ятниця'),
    )


class ClassLesson(models.Model):

    LESSONINDEXES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )
    SUBGROUPS = (
        ('1', '1'),
        ('2', '2'),
    )
    SPECWEEKS = (
        ('Nu', 'Чисельник'),
        ('De', 'Знаменник'),
    )
    day = models.CharField(
        'День',
        max_length=2,
        choices=WEEKDAYS,
    )
    index = models.CharField(
        'Номер уроку',
        max_length=1,
        choices=LESSONINDEXES,
    )
    title = models.ForeignKey(LessonList, on_delete=models.CASCADE)
    class_consisting = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name="lessons")
    lesson_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher_lessons")

    subgroup = models.CharField(
        'Підгрупа',
        max_length=1,
        choices=SUBGROUPS,
        blank=True,
        null=True
    )
    spec_week = models.CharField(
        'Тиждень',
        max_length=2,
        choices=SPECWEEKS,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.title.title
