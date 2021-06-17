# Generated by Django 2.2.13 on 2021-06-17 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20200707_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlesson',
            name='class_consisting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='schedule.ClassSchedule'),
        ),
        migrations.AlterField(
            model_name='classlesson',
            name='index',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=1, verbose_name='Номер уроку'),
        ),
        migrations.AlterField(
            model_name='classlesson',
            name='lesson_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_lessons', to='teachers.Teacher'),
        ),
    ]
