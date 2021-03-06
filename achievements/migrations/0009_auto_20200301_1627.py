# Generated by Django 2.2.2 on 2020-03-01 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0008_subject_winner'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Рік')),
            ],
            options={
                'verbose_name': 'Олімпіадний рік',
                'verbose_name_plural': 'Олімпіадні роки',
            },
        ),
        migrations.AddField(
            model_name='winner',
            name='stage',
            field=models.CharField(choices=[('s1', 'II (районний) етап'), ('s2', 'III (обласний) етап'), ('s3', 'II (обласний) етап МАН')], default='s1', max_length=2, verbose_name='Етап'),
        ),
        migrations.AlterField(
            model_name='winner',
            name='subject',
            field=models.CharField(max_length=20, verbose_name='Предмет'),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AddField(
            model_name='winner',
            name='year',
            field=models.ForeignKey(default=2001, on_delete=django.db.models.deletion.CASCADE, to='achievements.ContestYear'),
            preserve_default=False,
        ),
    ]
