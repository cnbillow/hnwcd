# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 12:33
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0052_auto_20161207_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='Content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='具体职务'),
        ),
    ]
