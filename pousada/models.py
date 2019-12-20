from django.urls import reverse
import locale
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .photo import *
from datetime import date


locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class CasadePedraCotacao(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, blank=False, null=False, unique=False)
    name2 = models.CharField(max_length=100, blank=False, null=False, unique=False)
    tel = PhoneNumberField()
    checkin = models.DateField(blank=False, null=False)
    checkout = models.DateField(blank=False, null=False)
    person_num = models.IntegerField(blank=False, null=False)
    kidquestion = models.IntegerField(blank=False, null=False)
    kid1 = models.IntegerField(blank=True, null=True)
    kid2 = models.IntegerField(blank=True, null=True)
    kid3 = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=False, null=False)
    dialy_of_price = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    portion = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    def cotacao_detail(self):
        return reverse('person_change', args=[self.id])

    def plus_discont(self):
        calculation = float(int((self.checkout - self.checkin).days) * self.dialy_of_price)
        return locale.currency(calculation + (calculation * (20 / 100)), grouping=True)

    # Calculos de Valores de Data
    def dialy_num(self):
        return int((self.checkout - self.checkin).days)

    # Calculo de Valor da Diaria
    def dialy_price(self):
        dialy = int((self.checkout - self.checkin).days)
        calculation = locale.currency(float((dialy * self.dialy_of_price)), grouping=True)
        return calculation

    # Calculo do desconto
    def discount_price(self):
        calculation = float(int((self.checkout - self.checkin).days) * self.dialy_of_price)
        return locale.currency(calculation - (calculation * (self.discount / 100)), grouping=True)


    # Valor de Diaria em forma Alfabetica 1 diaria = UMA Diaria
    def dialy_alfa(self):
        dialy = int((self.checkout - self.checkin).days)
        if dialy == 1:
            return 'UMA'
        elif dialy == 2:
            return 'DUAS'
        elif dialy == 3:
            return 'TRÊS'
        elif dialy == 4:
            return 'QUATRO'
        elif dialy == 5:
            return 'CINCO'
        elif dialy == 6:
            return 'SEISE'
        elif dialy == 7:
            return 'SETE'
        elif dialy == 8:
            return 'OITO'
        elif dialy == 9:
            return 'NOVE'
        elif dialy == 10:
            return 'DEZE'
        elif dialy == 11:
            return 'ONZE'
        elif dialy == 12:
            return 'DOZE'
        elif dialy == 13:
            return 'TRÊZE'
        elif dialy == 14:
            return 'QUARTORZE'
        elif dialy == 15:
            return 'QUINZE'
        elif dialy == 16:
            return 'DEZESSEIS'
        elif dialy == 17:
            return 'DEZESSETE'
        elif dialy == 18:
            return 'DEZOITO'
        elif dialy == 19:
            return 'DEZENOVE'
        elif dialy == 20:
            return 'VINTE'
        elif dialy == 21:
            return 'VINTE E UMA'
        elif dialy == 22:
            return 'VINTE E DUAS'
        elif dialy == 23:
            return 'VINTE E TRÊS'
        elif dialy == 24:
            return 'VINTE E QUATRO'
        elif dialy == 25:
            return 'VINTE E CINCO'
        elif dialy == 26:
            return 'VINTE E SEISE'
        elif dialy == 27:
            return 'VINTE E SETE'
        elif dialy == 28:
            return 'VINTE E OITO'
        elif dialy == 29:
            return 'VINTE E NOVE'
        elif dialy == 30:
            return 'TRINTA'
        elif dialy == 31:
            return 'TRINTA E UMA'
        else:
            return 'Erro!'

    # Valor de desconto Parcelado Dividido pelo valor...
    def portion_value(self):
        calculation = float(int((self.checkout - self.checkin).days) * self.dialy_of_price)
        #calculation2 = (calculation - (calculation * (self.discount / 100)))
        return locale.currency((calculation / self.portion), grouping=True)
    
    def valor_meio(self):
        calculation = float(int((self.checkout - self.checkin).days) * self.dialy_of_price / 2)
        #calculation2 = (calculation - (calculation * (self.discount / 100)))
        return locale.currency((calculation / self.portion), grouping=True)

    def parcelado2op(self):
        calculation = float(int((self.checkout - self.checkin).days) * self.dialy_of_price / self.portion)
        #calculation2 = (calculation - (calculation * (self.discount / 100)))
        return locale.currency((calculation / self.portion), grouping=True)

    def suite(self):
        if self.person_num <= 3:
            return "Luxo"
        else:
            return "Familly"

    def person_alfa(self):
        if self.person_num == 1:
            return 'Uma Pessoa'
        elif self.person_num == 2:
            return 'Duas Pessoas'
        elif self.person_num == 3:
            return 'Três Pessoas'
        elif self.person_num == 4:
            return 'Quatro Pessoas'
        elif self.person_num == 5:
            return 'Cinco Pessoas'
        elif self.person_num == 6:
            return 'Seis Pessoas'

    def telefone(self):
        tel = str(self.tel)
        ddi = tel[0:3]
        dd = tel[3:5]
        numero1 = tel[5:10]
        numero2 = tel[10:15]
        return ('{} ({}) {}-{}').format(ddi, dd, numero1, numero2)


    def teste(self):
        diaria = int((self.checkout - self.checkin).days)
        ttt = photo_normal(date.strftime(self.checkin, '%d/%m/%Y'), 
        date.strftime(self.checkout, '%d/%m/%Y'), 
        diaria, self.person_num,
        self.dialy_price(),
        self.valor_meio(),
        self.parcelado2op(),
        self.portion,
        self.parcelado2op(),
        self.portion,
        self.kidquestion,
        self.kid1,
        self.kid2,
        self.kid3,
        )
        #tt = (teste().format(valor1=self.dialy_price(), val_x=self.portion, val_entrada=self.portion_value(),parc_res=self.portion-1,parc_3op=self.portion,parc_3opc_2=self.portion,val_parc_3opc=self.portion_value(),val_avista=self.discount_price(),porc_desc=self.discount))
        #data = str(base64.b64encode(tt.encode()))
        return ttt

    def tes(self, valor):
        self.dialy_of_price_site = valor
        self.save()

class Pousada_Booking2(models.Model):
    nome_pousada = models.CharField(max_length=30, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Cotções_pousadasModels(models.Model):
    checkin = models.DateField(blank=False, null=False)
    checkout = models.DateField(blank=False, null=False)
    num_adultos = models.IntegerField(default=2, null=False)
    num_crianças = models.IntegerField(default=0, null=False)
    pousadas = models.CharField(max_length=300)






