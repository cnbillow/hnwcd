# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0025_auto_20161205_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='ProCateID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='women.ProCates'),
        ),
    ]
