# Generated by Django 2.0.2 on 2018-03-18 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0059_auto_20180318_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='image1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='image5',
        ),
    ]
