# Generated by Django 5.0.1 on 2024-05-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0005_rename_h_text_lavita_p_h1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
