# Generated by Django 4.2.6 on 2023-12-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cin', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('numtel', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('time', models.TimeField(null=True)),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
    ]
