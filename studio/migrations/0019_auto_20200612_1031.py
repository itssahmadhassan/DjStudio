# Generated by Django 3.0.6 on 2020-06-12 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0018_auto_20200612_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
