# Generated by Django 2.1 on 2019-04-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0031_team_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=models.SlugField(max_length=55),
        ),
    ]
