# Generated by Django 3.0.6 on 2020-06-08 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0015_auto_20200607_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='upload_video',
            field=models.FileField(blank=True, default='', null=True, upload_to='static/videos/'),
        ),
    ]
