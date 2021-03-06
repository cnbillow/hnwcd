# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0030_auto_20161205_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProNews',
            fields=[
                ('ProNewID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=56, verbose_name='标题')),
                ('Author', models.CharField(max_length=50, null=True, verbose_name='作者')),
                ('Content', models.TextField(verbose_name='内容')),
                ('PublishDate', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('ProID', models.IntegerField(default=0)),
                ('IsCheck', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '公益新闻',
                'verbose_name_plural': '公益新闻',
            },
        ),
    ]
