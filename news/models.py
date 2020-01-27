import telegram
from django.conf import settings
from django.template.loader import render_to_string
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from photogallery.models import Topic

def post_event_on_telegram(event):
    message_html = render_to_string('news/telegram_message.html', {
        'event': event
    })
    message_html = message_html.replace("<p>","").replace("</p>","\n")
    print(message_html)
    telegram_settings = settings.TELEGRAM
    bot = telegram.Bot(token=telegram_settings['bot_token'])
    bot.send_message(chat_id="@%s" % telegram_settings['channel_name'], text=message_html, parse_mode=telegram.ParseMode.HTML)          

class Article(models.Model):
    title = models.CharField('Назва', max_length = 40) 
    short_description = models.CharField('Короткий опис', max_length = 120)
    post = RichTextField('Опис')
    date = models.DateField('Дата')
    album = models.ForeignKey(Topic, on_delete = models.CASCADE, blank=True, null = True)
    image = models.ImageField('Фотографія', upload_to='post_image', blank=True)
    image_thumbnail = ImageSpecField(source='image', 
                                    processors=[ResizeToFill(340,180)],
                                    format='JPEG',
                                    options={'quality':60})

    objects = models.Manager()


    def save(self, *args, **kwargs):
        post_event_on_telegram(self)
        super(Article, self).save(*args, **kwargs)

                                                                            

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'