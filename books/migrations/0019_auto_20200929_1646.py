# Generated by Django 3.0.7 on 2020-09-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_auto_20200929_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booktags',
            options={'ordering': (
                'name',), 'verbose_name': 'book tag', 'verbose_name_plural': 'book tags'},
        ),
        migrations.AddField(
            model_name='booktags',
            name='category2',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'General fiction main'), (2, 'General fiction secondary'), (
                3, 'Non-fiction'), (4, 'Sci-fi and Fantasy'), (5, 'Children and Middle Grade'), (6, 'Teen and Young adult')], default=99, help_text='Tag category'),
        ),
    ]
