# Generated by Django 3.0.6 on 2020-06-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0008_auto_20200607_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='upload_pic',
            field=models.ImageField(blank=True, default='static/images/chiks.jpg', null=True, upload_to='static/images/'),
        ),
    ]
