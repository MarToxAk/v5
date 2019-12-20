from django import forms

from .models import PousadaModels, CotaçõesModels


class PousadaForms(forms.ModelForm):
    class Meta:
        model = PousadaModels
        fields = ('nome', 'link')


class CotaçõesForms(forms.ModelForm):
    

    pousadas = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=PousadaModels.objects.all())
    
    class Meta:
        model = CotaçõesModels
        fields = ('checkin', 'checkout', 'pousadas', 'num_adultos', 'num_crianças', 'pousadas', )

class Editar_Cotação_Forms(forms.ModelForm):
    

    pousadas = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=PousadaModels.objects.all())
    checkin = forms.CharField()
    checkout = forms.CharField()
    
    class Meta:
        model = CotaçõesModels
        fields = ('checkin', 'checkout', 'pousadas', 'num_adultos', 'num_crianças', 'pousadas', )

