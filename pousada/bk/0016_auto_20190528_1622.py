# Generated by Django 2.1.5 on 2019-05-28 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pousada', '0015_auto_20190130_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
        migrations.RenameField(
            model_name='blogcomments',
            old_name='val_diarias',
            new_name='val_diaria',
        ),
        migrations.RemoveField(
            model_name='blogcomments',
            name='diarias',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]