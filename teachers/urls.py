from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
    #path('', ListView.as_view(queryset=Article.objects.all().order_by('-date')[:6], template_name="news/allnews.html")),
    path('', views.methodical_work, name='methodical-work'),
    path('methodical-associations/<int:mo_id>/', views.mo),
    path('administration', views.administration),
    path('legal-framework', views.legal_framework),
    # path('pedagogics-perspective-plan', views.pedagogics_perspective_plan),
    path('pedagogical-certification', views.pedagogical_certification),
    #path('guidelines', views.guidelines),
] 