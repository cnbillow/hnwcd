# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 09:43
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0061_auto_20161209_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liuyans',
            name='IsShow',
            field=models.CharField(max_length=56, verbose_name='是否显示'),
        ),
        migrations.AlterField(
            model_name='liuyans',
            name='Reply',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', null='True', verbose_name='留言回复'),
        ),
    ]