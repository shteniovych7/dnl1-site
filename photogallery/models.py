from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import datetime

class Topic(models.Model):
    name = models.CharField('Назва', max_length=80)
    date = models.DateField('Дата', blank=True, default=datetime.date.today)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбоми'


class Photo(models.Model):
    description = models.CharField('Опис', max_length=100, null = True, blank = True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField('Фото', upload_to='photogallery/static/photogallery')
    image_thumbnail = ImageSpecField(source='image', 
                                    processors=[ResizeToFill(255,170)],
                                    format='JPEG',
                                    options={'quality':60})

    def get_source(self):
        directory = self.image.name.split('/static/')
        return directory[1]

    def get_name(self):
        directory = self.image.name.split('/')
        return directory[-1]

    def __str__(self):
        return self.get_name()
