# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 01:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20170123_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map',
            old_name='left_latitude',
            new_name='left_latitude_val',
        ),
        migrations.RenameField(
            model_name='map',
            old_name='left_longitude',
            new_name='left_longitude_val',
        ),
        migrations.RenameField(
            model_name='map',
            old_name='right_latitude',
            new_name='right_latitude_val',
        ),
        migrations.RenameField(
            model_name='map',
            old_name='right_longitude',
            new_name='right_longitude_val',
        ),
    ]
