# Generated by Django 3.0.7 on 2020-07-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0023_auto_20200717_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='upload_pic',
            field=models.ImageField(default='images/a2.jpg', upload_to='static/gallery/'),
        ),
    ]
