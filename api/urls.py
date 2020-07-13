from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('news/', views.NewsListView.as_view()),
    path('news/<int:pk>/', views.NewsDetailView.as_view()),
    path('schedule/', views.ScheduleListView.as_view()),
    path('schedule/<int:pk>', views.ScheduleDetailView.as_view()),
    path('teachers/', views.TeacherListView.as_view()),
    path('teachers/<int:pk>', views.TeacherScheduleView.as_view())
]
