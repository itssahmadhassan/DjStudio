# Generated by Django 3.0.6 on 2020-06-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0020_auto_20200624_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='upload_pic',
            field=models.ImageField(default='images/a2.jpg', upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='upload_video',
            field=models.FileField(blank=True, default='', null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='services',
            name='upload_pic',
            field=models.ImageField(blank=True, default='images/chiks.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='services',
            name='upload_video',
            field=models.FileField(blank=True, default='', null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='slider_pic_upload',
            field=models.ImageField(default='images/a2.jpg', upload_to='slider_pics'),
        ),
    ]
