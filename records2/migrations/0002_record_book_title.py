# Generated by Django 3.0.7 on 2020-06-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='book_title',
            field=models.CharField(default='title', max_length=200),
        ),
    ]