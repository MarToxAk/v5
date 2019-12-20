# Generated by Django 2.2.6 on 2019-10-20 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CotaçõesHospedeModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('num_adultos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CriançasDadoModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_crianças', models.IntegerField()),
                ('idade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ImagemWhatsAppModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TextoWhatsappModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ValorCotaçãoModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='HospedeModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('num_telefone', models.CharField(max_length=17)),
                ('cotações', models.ManyToManyField(to='cotacao.CotaçõesHospedeModels')),
            ],
        ),
        migrations.AddField(
            model_name='cotaçõeshospedemodels',
            name='crianças',
            field=models.ManyToManyField(to='cotacao.CriançasDadoModels'),
        ),
        migrations.AddField(
            model_name='cotaçõeshospedemodels',
            name='valor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotacao.ValorCotaçãoModels'),
        ),
    ]
