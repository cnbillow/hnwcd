# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 01:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0040_auto_20161206_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='CategoryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='women.Categories'),
        ),
    ]
