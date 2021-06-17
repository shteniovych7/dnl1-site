from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Lesson(models.Model):
    title = models.CharField('Назва', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField('Назва', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Rank(models.Model):
    title = models.CharField('Назва', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Звання'
        verbose_name_plural = 'Звання'


class SpecialPosition(models.Model):
    title = models.CharField('Назва', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Особливий статус'
        verbose_name_plural = 'Особливі статуси'


class MethodicalAssociation(models.Model):
    title = models.CharField('Назва', max_length = 150)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Предметно-методична комісія"
        verbose_name_plural = "Предметно-методичні комісії"


class Teacher(models.Model):
    DIRECTOR = 'dr'
    DEPUTY = 'dp'
    ADMINISTRATION_CHOICES = (
        (DIRECTOR, 'Директор'),
        (DEPUTY, 'Заступник директора')
    )

    first_name = models.CharField("Ім'я", max_length=20)
    fathers_name = models.CharField('По батькові', max_length = 20, default='1')
    second_name = models.CharField('Прізвище', max_length = 20)
    methodical_association = models.ManyToManyField(MethodicalAssociation)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    rank  = models.ForeignKey(Rank, on_delete = models.CASCADE, blank = True, null = True)
    # join_year = models.IntegerField('Рік приходу на роботу', default=1990)
    special_position = models.CharField(
        max_length=2,
        choices=ADMINISTRATION_CHOICES,
        blank=True,
        null=True
    )
    lesson = models.ManyToManyField(Lesson)
    photo = ProcessedImageField(upload_to='teacher_images', blank=True,
                                processors=[ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality': 90})

    objects = models.Manager()

    def __str__(self):
        return self.second_name + ' ' + self.first_name

    class Meta:
        verbose_name = 'Вчитель'
        verbose_name_plural = 'Вчителі'
        ordering = ['second_name']


class CourseRetraining(models.Model):
    year = models.IntegerField('Рік')

    objects = models.Manager()

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Курсова перепідготовка '
        verbose_name_plural = 'Курсова перепідготовка'
        ordering = ['-year']


class CourseRetrainingTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    year = models.ForeignKey(CourseRetraining, on_delete=models.CASCADE)
    start_time = models.DateField('Дата початку курсу')
    end_time = models.DateField('Дата завершення курсу')
    course_code = models.CharField("Код курсу", max_length=20)
    variant = models.CharField("Назва варіанту", max_length=20)
    course_name = models.CharField("Назва курсу", max_length=255)
    certificate_number = models.CharField("Номер сертифіката", max_length=255,  blank = True, null = True)


    def get_name(self):
        return self.teacher


    def __str__(self):
        return self.teacher.__str__()

    class Meta:
        verbose_name = 'Вчитель курсової перепідготовки'
        verbose_name_plural = 'Вчителі курсової перепідготовки'

