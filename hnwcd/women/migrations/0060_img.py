# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0059_auto_20161207_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', image_cropping.fields.ImageCropField(blank=True, upload_to='uploaded_images')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
            ],
        ),
    ]
