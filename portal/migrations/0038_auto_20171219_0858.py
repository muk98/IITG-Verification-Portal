# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0037_auto_20171219_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='record_progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_0', models.CharField(default='none', max_length=200)),
                ('stage_1', models.CharField(default='none', max_length=200)),
                ('stage_2', models.CharField(default='none', max_length=200)),
                ('stage_3', models.CharField(default='none', max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='progress',
            new_name='request_progress',
        ),
        migrations.AddField(
            model_name='record_progress',
            name='request_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.request_progress'),
        ),
    ]
