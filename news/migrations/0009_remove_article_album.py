# Generated by Django 2.2.2 on 2019-07-24 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_article_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='album',
        ),
    ]
