# Generated by Django 2.1.1 on 2018-09-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0011_auto_20180930_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='name_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='icon_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
