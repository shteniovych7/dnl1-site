from django.urls import path, include
from . import views
from django.views.generic import ListView
from news.models import Article


urlpatterns = [
    path('', ListView.as_view(queryset=Article.objects.all().order_by('-date')[:6], template_name="dnl1/homePage.html")),
    path('news/', include('news.urls')),
    path('distance_learning', include('distance_learning.urls')),
    path('methodical-work/', include('teachers.urls')),
    path('photo-gallery/', include('photogallery.urls')),
    path('about-us/', views.about_us),
    path('contacts/', views.contacts),
    path('achievements/', include('achievements.urls')),
    path('statut/', views.statut),
    path('entry-rules/', views.entry_rules),
    path('license/', views.license),
    path('vacancies/', views.vacancies),
    path('educational_programs/', views.educational_programs),
    path('inclination/', views.inclination),
    path('work-plan/', views.work_plan),
    path('pedagogical-meetings/', views.pedagogical_meetings),
    path('material-base/', views.material_base),
    path('orders/', views.orders),
    path('activity-report/', views.activity_report),
    path('financial-statements/', views.financial_statements),
    path('schedule/', views.schedule),
    path('educational-activities/', views.educational_activities),
    path('zno/', views.zno),
    path('social-service/', views.social_service),
    path('collective/', views.collective),
    path('year-structure/', views.year_structure),
    path('psychological-service/', views.psychological_service),
    path('medical-service/', views.medical_service),
    path('dining/', views.dining),
    path('library/', views.library),
    
]
