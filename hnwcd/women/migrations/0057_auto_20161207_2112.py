# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 13:12
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0056_auto_20161207_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrs',
            name='ImgURL',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='图片'),
        ),
    ]
