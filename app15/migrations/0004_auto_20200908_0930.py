# Generated by Django 2.2 on 2020-09-08 04:00

import app15.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app15', '0003_auto_20200908_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[app15.models.validate_name]),
        ),
    ]