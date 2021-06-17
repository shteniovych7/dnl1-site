from django.contrib import admin
from .models import Teacher, MethodicalAssociation, Category, Rank, SpecialPosition, Lesson, CourseRetraining, CourseRetrainingTeacher
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth

admin.site.site_header = 'ДНЛ №1'


class TeacherInline(admin.TabularInline):
    fieldsets = [
        ('teacher', {'fields': ['teacher']}),
        ('start_time', {'fields': ['start_time']}),
        ('end_time', {'fields': ['end_time']}),
        ('course_code', {'fields': ['course_code']}),
        ('variant', {'fields': ['variant']}),
        ('course_name', {'fields': ['course_name']}),
        ('certificate_number', {'fields': ['certificate_number']}),
    ]
    model = CourseRetrainingTeacher
    extra = 3


class CourseRetrainingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['year']}),
    ]
    inlines = [TeacherInline]


admin.site.register(CourseRetraining, CourseRetrainingAdmin)


#admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
admin.site.register(Teacher)
admin.site.register(MethodicalAssociation)
# admin.site.register(Category)
#admin.site.register(Rank)
#admin.site.register(SpecialPosition)
admin.site.register(Lesson)