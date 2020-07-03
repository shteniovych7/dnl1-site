from django.urls import path, include
from django.views.generic import ListView, DetailView
from news.models import Article
from . import views


urlpatterns = [
    # path('', ListView.as_view(queryset=Article.objects.all().order_by('-date')[:6], template_name="news/allnews.html")),
    path('', views.allnews, name='allnews'),
    path('<int:pk>/', DetailView.as_view(model = Article, template_name = "news/post.html"))
]
