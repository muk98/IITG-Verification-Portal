# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-15 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0023_auto_20171215_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='request_year',
            field=models.CharField(default='', max_length=200),
        ),
    ]