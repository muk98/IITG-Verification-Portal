# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0034_auto_20171219_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='send_by',
        ),
        migrations.DeleteModel(
            name='request',
        ),
    ]
