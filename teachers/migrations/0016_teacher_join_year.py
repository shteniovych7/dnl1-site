# Generated by Django 2.2.2 on 2019-08-31 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0015_auto_20190831_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='join_year',
            field=models.IntegerField(default=1990, verbose_name='Рік приходу на роботу'),
        ),
    ]