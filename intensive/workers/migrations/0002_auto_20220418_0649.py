# Generated by Django 3.2.12 on 2022-04-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Фамилия'),
        ),
    ]
