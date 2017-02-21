# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0012_auto_20161205_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liuyans',
            fields=[
                ('LId', models.AutoField(primary_key=True, serialize=False)),
                ('Content', models.TextField(verbose_name='留言内容')),
                ('IsShow', models.CharField(max_length=56, verbose_name='姓名')),
                ('Time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('Reply', models.TextField(verbose_name='留言回复')),
            ],
            options={
                'verbose_name_plural': '网友留言',
                'verbose_name': '网友留言',
            },
        ),
        migrations.AlterField(
            model_name='links',
            name='LinkURL',
            field=models.CharField(max_length=256, verbose_name='网址'),
        ),
    ]