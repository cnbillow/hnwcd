# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0063_auto_20170207_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liuyans',
            name='IsShow',
            field=models.CharField(default='false', max_length=56, null='True', verbose_name='是否显示'),
        ),
    ]