# Generated by Django 2.1.1 on 2018-09-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0005_manager_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
