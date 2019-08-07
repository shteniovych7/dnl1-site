from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='photogallery'),
    path('<int:topic_id>/', views.topic),
] 