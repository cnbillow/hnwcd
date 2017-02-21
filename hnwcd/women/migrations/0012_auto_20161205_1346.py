# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0011_donates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('LinkID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=56, verbose_name='姓名')),
                ('LinkURL', models.CharField(max_length=256, verbose_name='')),
                ('Rank', models.IntegerField(blank=True, unique=True, verbose_name='顺序')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.AlterModelOptions(
            name='donates',
            options={'verbose_name': '爱心捐赠', 'verbose_name_plural': '爱心捐赠'},
        ),
    ]
