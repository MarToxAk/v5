from django.urls import path, re_path
from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.urls import path, include  # new
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.Cotacao.as_view(), name='list'),
    path('add/', views.CotacaoCreat.as_view(), name='add'),
    path('list/<int:pk>/', views.CotacaoUpdate.as_view(template_name='pousada/casadepedracotacao_edit.html'), name='person_change2'),
    re_path(r'list/edit/(?P<pk>\d+)/$', views.CotacaoDetail.as_view(), name='person_change'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add2/', views.add2, name='add2'),
    path('cotacoes/', views.Cotações_pousadasViews.as_view(), name='cotaçoes'),
]

