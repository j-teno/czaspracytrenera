# Generated by Django 2.1.1 on 2019-07-13 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0034_auto_20190713_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='date_end',
            field=models.DateField(default=datetime.date(2020, 6, 30)),
        ),
    ]
