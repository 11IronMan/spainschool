# Generated by Django 5.0.1 on 2024-05-04 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0015_grafic_dont_work_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grafic',
            name='dont_work_days',
        ),
        migrations.AddField(
            model_name='work_day',
            name='dont_work_days',
            field=models.CharField(default='ВС', max_length=100),
        ),
    ]
