# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0014_auto_20161205_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='BranchID',
            field=models.IntegerField(blank=True, verbose_name='职务ID'),
        ),
    ]