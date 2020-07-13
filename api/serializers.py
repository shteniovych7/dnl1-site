from rest_framework import serializers
from news.models import Article
from schedule.models import ClassLesson, ClassSchedule
from teachers.models import Teacher


class NewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'short_description', 'date', 'image', )


class NewsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'post', 'date', 'image', )


class ClassLessonSerializer(serializers.ModelSerializer):
    lesson_teacher = serializers.SlugRelatedField(slug_field="first_name", read_only=True)

    class Meta:
        model = ClassLesson
        fields = '__all__'


class ClassScheduleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassSchedule
        fields = '__all__'


class ClassScheduleDetailSerializer(serializers.ModelSerializer):
    lessons = ClassLessonSerializer(many=True)

    class Meta:
        model = ClassSchedule
        fields = '__all__'


class TeacherListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'fathers_name', 'second_name')


class TeacherScheduleSerializer(serializers.ModelSerializer):
    teacher_lessons = ClassLessonSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'fathers_name', 'second_name', 'teacher_lessons')