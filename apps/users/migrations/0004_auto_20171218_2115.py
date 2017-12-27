# Generated by Django 2.0 on 2017-12-18 21:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171218_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发送时间'),
        ),
    ]
