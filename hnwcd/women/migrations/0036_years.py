# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0035_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Years',
            fields=[
                ('YearID', models.AutoField(primary_key=True, serialize=False)),
                ('YearName', models.CharField(max_length=10, verbose_name='年份')),
            ],
            options={
                'verbose_name': '年份',
                'verbose_name_plural': '年份',
            },
        ),
    ]