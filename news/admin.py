'''from django.contrib import admin
from news.models import Article


class ArticlesAdmin(admin.ModelAdmin):
    list_filter = ('date',)
    change_form_template = 'admin/articles/articles_change_form.html'

admin.site.register(Article, ArticlesAdmin)
'''

from django.contrib import admin
from news.models import Article
from image_cropping import ImageCroppingMixin

class ArticlesAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Article, ArticlesAdmin)