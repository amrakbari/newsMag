# Generated by Django 3.1.6 on 2021-02-15 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='author', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='cat', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 15, 12, 5, 9, 416396)),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
