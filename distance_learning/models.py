from django.db import models

class Task(models.Model):
    class_name = models.CharField('Клас', max_length = 40) 
    link = models.CharField('Посилання', max_length = 140, null=True) 

    objects = models.Manager()                               

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = 'Завдання для дистанційного вивчення'
        verbose_name_plural = 'Завдання для дистанційного вивчення'