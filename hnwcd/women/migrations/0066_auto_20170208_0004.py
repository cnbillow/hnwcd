# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0065_auto_20170208_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liuyans',
            name='IsShow',
            field=models.CharField(default=False, max_length=56, null='True', verbose_name='是否显示'),
        ),
    ]
