# Generated by Django 2.1.12 on 2019-09-28 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20190928_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 28, 17, 59, 31, 201825), verbose_name='Дата создания'),
        ),
    ]
