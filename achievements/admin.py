from django.contrib import admin
from .models import Medalist, AllMedalist, ContestYear, Winner


class MedalistInline(admin.TabularInline):
    fieldsets = [
        ('First name', {'fields': ['first_name']}),
        ('Second name', {'fields': ['second_name']}),
        ('Medalist type', {'fields': ['medalist_type']}),
    ]
    model = Medalist
    extra = 3


class AllMedalistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['year']}),
    ]
    inlines = [MedalistInline]


admin.site.register(AllMedalist, AllMedalistAdmin)

class WinnerInline(admin.TabularInline):
    fieldsets = [
        (None, {'fields': ['first_name', 'second_name', 'subject', 'class_n', 'teacher', 'place', 'stage']}),
    ]
    model = Winner
    extra = 3


class ContestYearAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['year']}),
    ]
    inlines = [WinnerInline]

admin.site.register(ContestYear, ContestYearAdmin)