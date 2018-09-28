# Generated by Django 2.0.2 on 2018-03-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0058_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='feedback',
            name='image2',
            field=models.ImageField(blank=True, default='media/feedback/none.png', upload_to='feedback/'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='image3',
            field=models.ImageField(blank=True, default='media/feedback/none.png', upload_to='feedback/'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='image4',
            field=models.ImageField(blank=True, default='media/feedback/none.png', upload_to='feedback/'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='image5',
            field=models.ImageField(blank=True, default='media/feedback/none.png', upload_to='feedback/'),
        ),
    ]
