# Generated by Django 2.1.5 on 2019-01-24 04:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pousada', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=96)),
                ('phone_number', models.CharField(max_length=12)),
                ('date_subscribed', models.DateTimeField(default=datetime.datetime(2019, 1, 24, 4, 7, 15, 587446))),
                ('messages_received', models.IntegerField(default=0)),
            ],
        ),
    ]
