# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-27 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0003_remove_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
    ]
