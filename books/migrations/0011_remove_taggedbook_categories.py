# Generated by Django 3.0.7 on 2020-09-28 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_taggedbook_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggedbook',
            name='categories',
        ),
    ]
