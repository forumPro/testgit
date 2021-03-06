# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('M', '\u7537\u6027'), ('F', '\u5973\u6027'), ('S', '\u4fdd\u5bc6')], max_length=20),
        ),
    ]
