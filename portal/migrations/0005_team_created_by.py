# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-11 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20171211_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_by',
            field=models.CharField(default='', max_length=200),
        ),
    ]