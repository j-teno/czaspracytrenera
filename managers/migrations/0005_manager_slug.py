# Generated by Django 2.1.1 on 2018-09-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0004_auto_20180922_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='slug',
            field=models.SlugField(default='fake', max_length=55),
            preserve_default=False,
        ),
    ]
