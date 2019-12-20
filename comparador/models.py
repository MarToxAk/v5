from django.db import models
from django.contrib.auth.models import User
from django.utils.formats import localize


class PousadaModels(models.Model):
    nome = models.CharField(max_length=40)
    link = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Valor_CotaçãoModels(models.Model):
    nome = models.CharField(max_length=40)
    cotacao = models.ForeignKey(PousadaModels, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

    def valor_monetario(self):
        valor = localize(self.valor)
        return valor

class CotaçõesModels(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    num_adultos = models.IntegerField()
    num_crianças = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pousadas = models.ManyToManyField(PousadaModels)
    valor = models.ManyToManyField(Valor_CotaçãoModels)



