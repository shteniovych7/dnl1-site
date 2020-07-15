from rest_framework import serializers
from rest_framework.serializers import ImageField
from news.models import Article
from schedule.models import ClassLesson, ClassSchedule
from teachers.models import Teacher


class NewsListSerializer(serializers.ModelSerializer):
    image_thumbnail = ImageField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class NewsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'post', 'date', 'image', )


class TeacherListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'fathers_name', 'second_name')


class ClassLessonSerializer(serializers.ModelSerializer):
    lesson_teacher = TeacherListSerializer()

    class Meta:
        model = ClassLesson
        fields = '__all__'


class TeacherScheduleSerializer(serializers.ModelSerializer):
    teacher_lessons = ClassLessonSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'fathers_name', 'second_name', 'teacher_lessons')




class ClassScheduleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassSchedule
        fields = '__all__'


class ClassScheduleDetailSerializer(serializers.ModelSerializer):
    lessons = ClassLessonSerializer(many=True)

    class Meta:
        model = ClassSchedule
        fields = '__all__'