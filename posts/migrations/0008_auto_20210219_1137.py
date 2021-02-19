# Generated by Django 3.1.6 on 2021-02-19 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0007_auto_20210219_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 19, 11, 37, 54, 102438)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='posts'),
        ),
    ]
