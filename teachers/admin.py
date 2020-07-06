from django.contrib import admin
from .models import Teacher, MethodicalAssociation, Category, Rank, SpecialPosition, Lesson
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth

admin.site.site_header = 'ДНЛ №1'


#admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
admin.site.register(Teacher)
admin.site.register(MethodicalAssociation)
#admin.site.register(Category)
#admin.site.register(Rank)
#admin.site.register(SpecialPosition)
admin.site.register(Lesson)