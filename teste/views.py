from django.shortcuts import render
from django.http import HttpResponse
from .models import TextoModels
from django.views.generic import View, ListView, TemplateView
# Create your views here.

class TextoViews(ListView):
    model = TextoModels
    template_name = 'teste.html'