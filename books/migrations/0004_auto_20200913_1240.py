# Generated by Django 3.0.7 on 2020-09-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200912_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance2',
            name='isbn13',
            field=models.CharField(
                blank=True, db_index=True, max_length=13, null=True),
        ),
    ]