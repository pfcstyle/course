# Generated by Django 2.0 on 2017-12-17 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 17, 22, 7, 43, 991384), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 17, 22, 7, 43, 993385), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 17, 22, 7, 43, 992385), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 17, 22, 7, 43, 993385), verbose_name='添加时间'),
        ),
    ]