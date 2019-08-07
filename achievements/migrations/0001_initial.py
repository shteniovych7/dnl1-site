# Generated by Django 2.2.2 on 2019-07-30 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medalist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievements.Year')),
            ],
        ),
    ]
