# Generated by Django 3.0.6 on 2020-06-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0005_services_upload_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='upload_pic',
            field=models.ImageField(blank=True, default='static/images/cat.jpg', null=True, upload_to='studio/static/images/'),
        ),
    ]
