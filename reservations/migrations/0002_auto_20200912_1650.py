# Generated by Django 3.0.7 on 2020-09-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='user_id',
            field=models.IntegerField(db_index=True),
        ),
    ]