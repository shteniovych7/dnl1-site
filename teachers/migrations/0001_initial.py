# Generated by Django 2.2.2 on 2019-06-09 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MethodicalAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('methodical_association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.MethodicalAssociation')),
            ],
        ),
    ]
