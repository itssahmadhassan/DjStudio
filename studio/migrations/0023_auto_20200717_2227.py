# Generated by Django 3.0.7 on 2020-07-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0022_auto_20200717_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='upload_pic',
            field=models.ImageField(default='images/a2.jpg', upload_to="{% static 'gallery' %}"),
        ),
    ]
