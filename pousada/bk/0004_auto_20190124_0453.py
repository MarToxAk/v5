# Generated by Django 2.1.5 on 2019-01-24 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pousada', '0003_auto_20190124_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 4, 53, 1, 711539)),
        ),
    ]
