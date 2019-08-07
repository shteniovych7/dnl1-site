# Generated by Django 2.2.2 on 2019-07-15 16:02

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0009_teacher_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='teacher_images'),
        ),
    ]
