from django.db import models


#__Inicio__
#Seção de Configuração
class TextoWhatsappModels(models.Model):
    texto = models.TextField()
    check_in = models.DateField(default=None)
    check_out = models.DateField(default=None)

    def __str__(self):
        self.texto


class ImagemWhatsAppModels(models.Model):
    img = models.TextField()
#__Fim__

#__Inicio__
#Banco de dados
class CriançasDadoModels(models.Model):
    num_crianças = models.IntegerField()
    idade = models.IntegerField()


class CotaçõesHospedeModels(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    num_adultos = models.IntegerField()
    crianças = models.ManyToManyField(CriançasDadoModels, db_table=None)


class ValorCotaçãoModels(models.Model):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    models.ForeignKey(CotaçõesHospedeModels, on_delete=models.CASCADE)


class HospedeModels(models.Model):
    nome = models.CharField(max_length=100)
    num_telefone = models.CharField(max_length=17)
    cotações = models.ManyToManyField(CotaçõesHospedeModels, db_table=None)

    def __str__(self):
        self.nome
#__Fim__