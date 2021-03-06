# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 07:51
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0060_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '700x700', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='img',
            name='image',
            field=image_cropping.fields.ImageCropField(blank=True, upload_to='uploaded/images/'),
        ),
    ]
