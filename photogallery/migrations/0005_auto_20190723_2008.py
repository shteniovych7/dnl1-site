# Generated by Django 2.2.2 on 2019-07-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0004_auto_20190723_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
