# Generated by Django 2.2.2 on 2019-07-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0011_auto_20190724_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='special_position',
            field=models.CharField(blank=True, choices=[('dr', 'Директор'), ('dp', 'Заступник директора')], max_length=2, null=True),
        ),
    ]
