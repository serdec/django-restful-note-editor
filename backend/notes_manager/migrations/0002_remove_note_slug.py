# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-11-14 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='slug',
        ),
    ]
