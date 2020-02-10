from django.db import models
from ckeditor.fields import RichTextField

class Task(models.Model):
    class_name = models.CharField('Клас', max_length = 40) 
    task = RichTextField('Завдання')

    objects = models.Manager()                               

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'