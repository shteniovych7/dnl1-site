# Generated by Django 2.2.2 on 2019-07-24 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0007_auto_20190724_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
