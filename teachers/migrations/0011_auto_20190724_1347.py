# Generated by Django 2.2.2 on 2019-07-24 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0010_teacher_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='special_position',
            field=models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.SpecialPosition'),
        ),
    ]
