# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-09 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20170209_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
