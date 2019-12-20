from django.shortcuts import render, redirect
from .forms import CasadePedraCotacaoForm
from .models import CasadePedraCotacao, Cotções_pousadasModels
from .forms import Cotações_pousadasForms
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from .entidades.tarefas import Tarefas
from .services import tafera_service


def index(request):
    return render(request, 'index.html', )



class Cotacao(GroupRequiredMixin, ListView):
    group_required = [u"editors", u"admins"]
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = CasadePedraCotacao
    context_object_name = 'people'
    paginate_by = 6
    def get_queryset(self):
        return CasadePedraCotacao.objects.order_by('-updated_at')


class CotacaoDetail(GroupRequiredMixin, DetailView):
    group_required = [u"editors", u"admins"]
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = CasadePedraCotacao
    context_object_name = 'dados'


class CotacaoUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u"editors", u"admins"]
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = CasadePedraCotacao
    form_class = CasadePedraCotacaoForm
    context_object_name = 'people'
    success_url = reverse_lazy('list')


class CotacaoCreat(GroupRequiredMixin, CreateView):
    group_required = [u"editors", u"admins"]
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = CasadePedraCotacao
    form_class = CasadePedraCotacaoForm

    def post(self, request):
        form = CasadePedraCotacaoForm(request.POST)

        if form.is_valid():
            author = form.cleaned_data['author']
            name = form.cleaned_data['name']
            tel = form.cleaned_data['tel']
            checkin = form.cleaned_data['checkin']
            checkout = form.cleaned_data['checkout']
            person_num = form.cleaned_data['person_num']
            kidquestion = form.cleaned_data['kidquestion']
            kid1 = form.cleaned_data['kid1']
            kid2 = form.cleaned_data['kid2']
            kid3 = form.cleaned_data['kid3']
            discount = form.cleaned_data['discount']
            portion = form.cleaned_data['portion']
            checkin2 = checkin.strftime(f"{'%d':0>2}{'%m':0>2}%Y")
            checkout2 = checkout.strftime(f"{'%d':0>2}{'%m':0>2}%Y")
            valordosite2 = tafera_service.webdrive(checkin=checkin2, checkout=checkout2, person_num=person_num, kidquestion=kidquestion, kid1=kid1, kid2=kid2, kid3=kid3)
            dialy_of_price = valordosite2
            tarefa_nova = Tarefas(author=author, name=name, tel=tel, checkin=checkin, checkout=checkout,
                                  person_num=person_num, kidquestion=kidquestion, kid1=kid1, kid2=kid2, kid3=kid3, discount=discount,
                                  dialy_of_price=dialy_of_price, portion=portion)
            tafera_service.cadastra_cotação(tarefa_nova)
            return redirect('list')
        else:
            form = CasadePedraCotacaoForm()



def teste(request):
    form = CasadePedraCotacaoForm()
    if request.method == 'POST':
        form = CasadePedraCotacaoForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/thanks/')
        else:
            form = CasadePedraCotacaoForm()
    return render(request, 'teste.html', {'form': form})


def add2(request):
    if request.method == 'POST':
        form = CasadePedraCotacaoForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            name = form.cleaned_data['name']
            tel = form.cleaned_data['tel']
            checkin = form.cleaned_data['checkin']
            checkout = form.cleaned_data['checkout']
            person_num = form.cleaned_data['person_num']
            kidquestion = form.cleaned_data['kidquestion']
            kid1 = form.cleaned_data['kid1']
            kid2 = form.cleaned_data['kid2']
            kid3 = form.cleaned_data['kid3']
            discount = form.cleaned_data['discount']
            dialy_of_price = form.cleaned_data['dialy_of_price']
            portion = form.cleaned_data['portion']
            dialy_of_price_site = 154.5
            tarefa_nova = Tarefas(author=author, name=name, tel=tel, checkin=checkin, checkout=checkout,
                                  person_num=person_num, kidquestion=kidquestion, kid1=kid1, kid2=kid2, kid3=kid3, discount=discount,
                                  dialy_of_price=dialy_of_price, dialy_of_price_site=dialy_of_price_site,
                                  portion=portion)
            tafera_service.cadastra_cotação(tarefa_nova)
            return redirect('list')
    else:
        form = CasadePedraCotacaoForm()

    return render(request, 'add2.html', {'form':form})


class Cotações_pousadasViews(CreateView):
    model =  Cotções_pousadasModels
    form_class = Cotações_pousadasForms


