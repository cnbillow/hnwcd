# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 12:31
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0051_auto_20161207_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liuyans',
            name='Content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='留言内容'),
        ),
        migrations.AlterField(
            model_name='liuyans',
            name='Reply',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='留言回复'),
        ),
    ]
