from django.conf.urls import url, include
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='inicio'), name='home'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'sair/$', views.Logout_Views.as_view(), name='sair' ),
    url(r'sair/sucesso/$', views.logout_sucesso, name='logout_sucesso'),
    url(r'cotações/$', views.ListaCotações_Views.as_view(), name='lista_cotação'),
    url(r'index/$', views.IndexViews.as_view(), name='inicio'),
    url(r'cotações/pousada/nova/$', views.Nova_Pousada_Views.as_view(), name='nova_pousada'),
    url(r'cotações/nova/$', views.Nova_Cotação_Views.as_view(), name='nova_cotação'),
    url(r'^cotações/editar/(?P<pk>\d+)', views.Editar_Cotação_Views.as_view(), name='editar_todas_cotações'),
    url(r'^cotações/apagar/(?P<pk>\d+)', views.CotaçõesDelete_Views.as_view(), name='cotação_delete'),
    url(r'^cotações/pousada/editar/(?P<pk>\d+)', views.Editar_Pousada_Views.as_view(), name='editar_pousada'),
]
