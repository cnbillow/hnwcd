# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 13:03
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0054_auto_20161207_2042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='procates',
            options={'verbose_name': '公益类型', 'verbose_name_plural': '公益类型'},
        ),
        migrations.AlterField(
            model_name='procates',
            name='Name',
            field=models.CharField(max_length=56, verbose_name='公益类型'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='Content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='IsCheck',
            field=models.CharField(choices=[('1', '是'), ('0', '否')], default='0', max_length=1, verbose_name='是否审核'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='IsFriend',
            field=models.CharField(choices=[('true', '是'), ('false', '否')], default='false', max_length=5),
        ),
        migrations.AlterField(
            model_name='projects',
            name='IsIndex',
            field=models.CharField(choices=[('true', '是'), ('false', '否')], default='false', max_length=5, verbose_name='是否置顶'),
        ),
    ]
