from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, FormView, RedirectView, TemplateView
from .entidades.tarefas import Tarefas, Tarefas_Update
from .forms import CotaçõesForms, PousadaForms, Editar_Cotação_Forms
from .models import CotaçõesModels, PousadaModels, Valor_CotaçãoModels
from .servicos import tarefas_servico
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

class ListaCotações_Views(LoginRequiredMixin, ListView):
    login_url  =  '/login/' 
    redirect_field_name  =  'redirect_to'
    model = CotaçõesModels
    template_name = 'cotacoes/lista_cotacao.html'

class Nova_Cotação_Views(LoginRequiredMixin, CreateView):
    model = CotaçõesModels
    form_class = CotaçõesForms
    template_name = 'cotacoes/cotacao_form.html'
    def form_valid(self, form):
        checkin = form.cleaned_data['checkin']
        checkout = form.cleaned_data['checkout']
        num_adultos = form.cleaned_data['num_adultos']
        num_crianças = form.cleaned_data['num_crianças']
        form.instance.user = self.request.user
        pousadas = form.cleaned_data['pousadas']
        tarefa_nova = Tarefas(checkin=checkin, checkout=checkout, num_adultos=num_adultos,
                            num_crianças=num_crianças, user=form.instance.user, pousadas=pousadas)
        tarefas_servico.CotaçõesServiços(tarefa_nova)
        return redirect('lista_cotação')


class Nova_Pousada_Views(LoginRequiredMixin, CreateView):
    model = PousadaModels
    form_class = PousadaForms
    template_name = 'cotacoes/pousada_form.html'
    def post(self, request, *args, **kwargs):
        form = PousadaForms(request.POST)
        if form.is_valid():
            pousada = form.save(commit=False)
            pousada.user = request.user
            pousada.save()
            return redirect('lista_cotação')
        else:
            form = PousadaForms()
        

class Editar_Cotação_Views(LoginRequiredMixin, UpdateView):
    model = CotaçõesModels
    form_class = CotaçõesForms
    template_name = 'cotacoes/edit_cotacao_form.html'    
    success_url = '/'
    def form_valid(self, form):
        checkin = form.cleaned_data['checkin']
        checkout = form.cleaned_data['checkout']
        num_adultos = form.cleaned_data['num_adultos']
        num_crianças = form.cleaned_data['num_crianças']
        form.instance.user = self.request.user
        pousadas = form.cleaned_data['pousadas']
        form.instance.id = form.instance.pk
        tarefa_nova = Tarefas_Update(checkin=checkin, checkout=checkout, num_adultos=num_adultos,
                            num_crianças=num_crianças, user=form.instance.user, pousadas=pousadas, id=form.instance.id)
        tarefas_servico.update_cotação(tarefa_nova)
        return HttpResponseRedirect(self.get_success_url())
    
            
class Editar_Pousada_Views(LoginRequiredMixin, UpdateView):
    model = PousadaModels
    form_class = PousadaForms
    template_name = 'cotacoes/pousada_form.html'
    success_url = '/'
    

class CotaçõesDelete_Views(DeleteView):
    model = CotaçõesModels
    success_url = '/'
    template_name = 'cotacoes/cotacoes_delete.html'
    

class Logout_Views(RedirectView):
    url = 'sucesso'
    template_name = 'registration/logout.html'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(Logout_Views, self).get(request, *args, **kwargs)

def logout_sucesso(request):
    latest_question_list = ''
    template = loader.get_template('registration/logout.html')
    context = {
    'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

class IndexViews(LoginRequiredMixin, TemplateView):
    template_name = 'cotacoes/index.html'
    