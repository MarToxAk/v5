# Generated by Django 2.1.5 on 2019-01-24 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pousada', '0006_auto_20190124_0608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomments',
            old_name='firstname',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='blogcomments',
            name='comment',
        ),
        migrations.AddField(
            model_name='blogcomments',
            name='n_pessoas',
            field=models.IntegerField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='blogcomments',
            name='valor_disconto',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]