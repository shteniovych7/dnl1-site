# Generated by Django 2.2.2 on 2020-02-10 19:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=40, verbose_name='Назва')),
                ('task', ckeditor.fields.RichTextField(verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Завдання',
                'verbose_name_plural': 'Завдання',
            },
        ),
    ]
