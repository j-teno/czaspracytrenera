# Generated by Django 3.0.3 on 2020-02-29 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0038_auto_20190721_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='date_end',
            field=models.DateField(default=datetime.date(2021, 6, 30)),
        ),
        migrations.AlterField(
            model_name='season',
            name='date_start',
            field=models.DateField(default=datetime.date(2020, 7, 1)),
        ),
        migrations.AlterField(
            model_name='season',
            name='slug',
            field=models.SlugField(blank=True, max_length=55, unique=True),
        ),
        migrations.AddConstraint(
            model_name='employment',
            constraint=models.UniqueConstraint(condition=models.Q(still_hired='True'), fields=('manager',), name='unique_manager_hired'),
        ),
        migrations.AddConstraint(
            model_name='employment',
            constraint=models.UniqueConstraint(condition=models.Q(still_hired='True'), fields=('team', 'role'), name='unique_team_hired'),
        ),
    ]
