# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abouts',
            fields=[
                ('AbID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=256, verbose_name='标题')),
                ('Content', models.TextField(verbose_name='内容')),
                ('PublishDate', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('Rank', models.IntegerField(blank=True, unique=True, verbose_name='顺序')),
            ],
            options={
                'verbose_name_plural': '关于我们',
                'verbose_name': '关于我们',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('ArticleID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=256, verbose_name='文章标题')),
                ('Author', models.CharField(max_length=256, verbose_name='作者')),
                ('Content', models.TextField(verbose_name='文章内容')),
                ('PublishDate', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('CategoryID', models.IntegerField(verbose_name='类别')),
                ('isCheck', models.IntegerField(default=1)),
                ('isTop', models.IntegerField(default=0)),
                ('Count', models.IntegerField(default=1, null=True)),
            ],
            options={
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('BranchID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50, verbose_name='姓名')),
                ('Content', models.TextField(verbose_name='内容')),
                ('Rank', models.IntegerField(blank=True, unique=True, verbose_name='顺序')),
            ],
            options={
                'verbose_name_plural': '理事会机构',
                'verbose_name': '理事会机构',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('CategoryID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20, verbose_name='类别')),
            ],
            options={
                'ordering': ['CategoryID'],
                'verbose_name_plural': '类别名称',
                'verbose_name': '类别名称',
            },
        ),
    ]
