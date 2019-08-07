from django.contrib import admin
from .models import Medalist, AllMedalist


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