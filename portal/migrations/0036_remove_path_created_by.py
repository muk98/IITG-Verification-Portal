# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 07:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0035_auto_20171219_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='path',
            name='created_by',
        ),
    ]
