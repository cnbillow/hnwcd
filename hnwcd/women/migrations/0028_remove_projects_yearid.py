# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 16:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0027_auto_20161205_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='YearID',
        ),
    ]
