# Generated by Django 3.0.6 on 2020-06-12 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0017_gallery_upload_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='degree',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='who_am_i',
            field=models.TextField(max_length=200),
        ),
    ]
