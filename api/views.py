from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NewsListSerializer, NewsDetailSerializer, ClassLessonSerializer, ClassScheduleListSerializer, ClassScheduleDetailSerializer, TeacherListSerializer, TeacherScheduleSerializer
from news.models import Article
from schedule.models import ClassLesson, ClassSchedule
from teachers.models import Teacher


class NewsListView(APIView):
    def get(self, request):
        news = Article.objects.all().order_by('-date')
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)


class NewsDetailView(APIView):
    def get(self, request, pk):
        news = Article.objects.get(id=pk)
        serializer = NewsDetailSerializer(news)
        return Response(serializer.data)


class ScheduleListView(APIView):
    def get(self, request):
        lessons = ClassSchedule.objects.in_class_growing_order()
        serializer = ClassScheduleListSerializer(lessons, many=True)
        return Response(serializer.data)


class ScheduleDetailView(APIView):
    def get(self, request, pk):
        lessons = ClassSchedule.objects.get(id=pk)
        serializer = ClassScheduleDetailSerializer(lessons)
        return Response(serializer.data)


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherListSerializer(teachers, many=True)
        return Response(serializer.data)


class TeacherScheduleView(APIView):
    def get(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = TeacherScheduleSerializer(teacher)
        return Response(serializer.data)
