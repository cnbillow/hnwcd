# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0010_auto_20161205_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donates',
            fields=[
                ('Donate', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=56, verbose_name='姓名')),
                ('Time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('Money', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='捐赠金额')),
            ],
        ),
    ]
