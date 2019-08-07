from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from photogallery.models import Topic

class Article(models.Model):
    title = models.CharField(max_length = 40) 
    short_description = models.CharField(max_length = 120)
    post = RichTextField()
    date = models.DateField()
    album = models.ForeignKey(Topic, on_delete = models.CASCADE, blank=True, null = True)
    image = models.ImageField(upload_to='post_image', blank=True)
    image_thumbnail = ImageSpecField(source='image', 
                                    processors=[ResizeToFill(340,180)],
                                    format='JPEG',
                                    options={'quality':60})

    objects = models.Manager()

    def __str__(self):
        return self.title
