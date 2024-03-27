# Generated by Django 3.0.7 on 2020-09-10 21:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('reservation_date', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('can_collect', models.BooleanField(default=False)),
                ('reservation_expiry', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
    ]
