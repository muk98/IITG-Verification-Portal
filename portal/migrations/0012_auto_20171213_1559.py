# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-13 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='stage1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='path',
            name='stage2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='path',
            name='stage3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='path',
            name='stage4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='path',
            name='stage5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]