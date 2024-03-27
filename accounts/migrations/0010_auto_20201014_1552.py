# Generated by Django 3.0.7 on 2020-10-14 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20201014_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='memb_num',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, validators=
                [django.core.validators.MinValueValidator(
                1), django.core.validators.MaxValueValidator(999)], verbose_name='membership number'),
        ),
    ]
