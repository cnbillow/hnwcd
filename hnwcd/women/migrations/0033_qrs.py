# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0032_auto_20161205_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qrs',
            fields=[
                ('QID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=56, verbose_name='名字')),
                ('ImgURL', models.CharField(max_length=50, verbose_name='图片链接')),
            ],
            options={
                'verbose_name_plural': '滚动图',
                'verbose_name': '滚动图',
            },
        ),
    ]
