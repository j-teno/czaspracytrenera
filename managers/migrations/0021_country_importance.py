# Generated by Django 2.1.2 on 2018-11-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0020_auto_20181102_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='importance',
            field=models.IntegerField(default=0),
        ),
    ]