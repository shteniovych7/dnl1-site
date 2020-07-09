from django.contrib import admin
from news.models import Article
import telegram
from django.conf import settings
from django.template.loader import render_to_string


@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    actions = ["post_event_on_telegram"]

    def post_event_on_telegram(self, request, queryset):
        if not settings.DEBUG:
            for news in queryset:
                message_html = render_to_string('news/telegram_message.html', {
                    'event': news
                })
                message_html = message_html.replace("<p>", "").replace("</p>", "\n")
                telegram_settings = settings.TELEGRAM
                bot = telegram.Bot(token=telegram_settings['bot_token'])
                bot.sendPhoto(chat_id="@%s" % telegram_settings['channel_name'], photo=news.image.url, caption=message_html,
                              parse_mode=telegram.ParseMode.HTML)
            self.message_user(request, "Бот відправив повідомлення")
        else:
            self.message_user(request, "Відправляти можна тільки в production!")

    post_event_on_telegram.short_description = "Відправити ботом в телеграм"
