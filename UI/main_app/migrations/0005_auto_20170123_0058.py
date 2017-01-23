# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_map_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='left_latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='left_longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='right_latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='right_longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]