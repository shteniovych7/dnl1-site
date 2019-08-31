from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class Lesson(models.Model):
    title = models.CharField('Назва', max_length = 150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Category(models.Model):
    title = models.CharField('Назва', max_length = 150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class Rank(models.Model):
    title = models.CharField('Назва', max_length = 150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Звання'
        verbose_name_plural = 'Звання'

class SpecialPosition(models.Model):
    title = models.CharField('Назва', max_length = 150)

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
        verbose_name = "Методичне об'єднання"
        verbose_name_plural = "Методичні об'єднання"


class Teacher(models.Model):
    DIRECTOR = 'dr'
    DEPUTY = 'dp'
    ADMINISTRATION_CHOICES = (
        (DIRECTOR, 'Директор'),
        (DEPUTY, 'Заступник директора')
    )

    first_name = models.CharField("Ім'я", max_length = 20)
    second_name = models.CharField('Прізвище', max_length = 20)
    methodical_association = models.ManyToManyField(MethodicalAssociation)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    rank  = models.ForeignKey(Rank, on_delete = models.CASCADE, blank = True, null = True)
    special_position = models.CharField(
        max_length=2,
        choices=ADMINISTRATION_CHOICES,
        blank=True,
        null=True
    )
    lesson = models.ManyToManyField(Lesson)
    photo = ProcessedImageField(upload_to='teacher_images', blank=True,
                                processors=[ResizeToFill(200,200)],
                                format='JPEG',
                                options={'quality':90})

    objects = models.Manager()

    def __str__(self):
        return self.second_name

    class Meta:
        verbose_name = 'Вчитель'
        verbose_name_plural = 'Вчителі'