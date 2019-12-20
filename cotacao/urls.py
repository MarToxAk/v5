from django.conf.urls import url, include
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    #url(r'^$', RedirectView.as_view(pattern_name='inicio'), name='home'),
    url('add/hospede', views.HospedeViews.as_view(), name='hospede'),
    url('add/cotacao', views.CotaçãoViews.as_view(), name='cotação'),
    url('config/wpp', views.TextoWhatsappViews.as_view(), name='configwpp'),
]
