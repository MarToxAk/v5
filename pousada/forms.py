import datetime
from datetime import timezone
from django import forms
from .models import CasadePedraCotacao, Cotções_pousadasModels, Pousada_Booking2
from phonenumber_field.modelfields import PhoneNumberField
from selenium import webdriver


CHOICES1 = (
    ('1', 'Uma Pessoa'),
    ('2', 'Duas Pessoas'),
    ('3', 'Três Pessoas'),
    ('4', 'Quatro Pessoas'),
    ('5', 'Cinco Pessoas'),
    ('6', 'Seis Pessoas')
)

CHOICES2 = (
    ('0', 'Sem Disconto'),
    ('5', "5% de Desconto"),
    ('10', '10% de Desconto'),
)
CHOICES3 = (
    ('1', 'À vista'),
    ('2', "2 Parcelas"),
    ('3', '3 Parcelas'),
    ('4', '4 Parcelas'),
    ('5', '5 Parcelas'),
)
CHOICES4 = (
    ('0', 'Menos de 1 Ano'),
    ('1', '1 Ano'),
    ('2', "2 Anos"),
    ('3', '3 Anos'),
    ('4', '4 Anos'),
    ('5', '5 Anos'),
    ('6', '6 Anos'),
)
CHOICES5 = (
    ('não', "não"),
    ('sim', 'sim'),
)

class CasadePedraCotacaoForm(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=100)
    #checkin = forms.DateField(label='Check In', widget=forms.SelectDateWidget(), initial=datetime.datetime.now())
    #checkout = forms.DateField(label='Check Out', widget=forms.SelectDateWidget(),
                               #initial=(datetime.datetime.now() + datetime.timedelta(1)))
    person_num = forms.ChoiceField(label='Numero de Pessoas', choices=CHOICES1, required=True, widget=forms.Select())
    discount = forms.ChoiceField(label='Disconto Inicial', choices=CHOICES2, widget=forms.Select)
    tel = PhoneNumberField()
    portion = forms.ChoiceField(label='Numero de parcelas', choices=CHOICES3, widget=forms.Select)
    #kidquestion = forms.ChoiceField(label='Tem Criança', choices=CHOICES5, widget=forms.Select)

    class Meta:
        model = CasadePedraCotacao
        fields = ['author', 'name', 'tel', 'checkin', 'checkout', 'person_num', 'kidquestion','kid1','kid2','kid3', 'discount', 'portion']




class Cotações_pousadasForms(forms.ModelForm):

    class Meta:
        model = Cotções_pousadasModels
        fields = ['checkin', 'checkout', 'num_adultos', 'num_crianças', 'pousadas']

    def __init__(self, user, *args, **kwargs):
        super(Cotações_pousadasForms, self).__init__(*args, **kwargs)
        self.fields['pousadas'].queryset = Pousada_Booking2.objects.filter(user=user)
