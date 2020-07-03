from django.contrib import admin
from .models import ClassLesson, ClassSchedule


class LessonInline(admin.TabularInline):
    model = ClassLesson
    extra = 27


class ClassScheduleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['class_title']}),
    ]
    inlines = [LessonInline]


admin.site.register(ClassSchedule, ClassScheduleAdmin)
