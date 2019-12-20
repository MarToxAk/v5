# Generated by Django 2.2.5 on 2019-09-15 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comparador', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cotaçõesmodels',
            old_name='num_adults',
            new_name='num_adultos',
        ),
        migrations.RemoveField(
            model_name='cotaçõesmodels',
            name='pousadas',
        ),
        migrations.AddField(
            model_name='cotaçõesmodels',
            name='pousadas',
            field=models.ManyToManyField(to='comparador.PousadaModels'),
        ),
        migrations.CreateModel(
            name='Valor_CotaçãoModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cotacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comparador.PousadaModels')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cotaçõesmodels',
            name='valor',
            field=models.ManyToManyField(to='comparador.Valor_CotaçãoModels'),
        ),
    ]