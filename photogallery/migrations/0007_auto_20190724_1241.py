# Generated by Django 2.2.2 on 2019-07-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0006_topic_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
