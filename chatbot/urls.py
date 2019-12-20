from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path

app_name = 'chatbot'

urlpatterns = [
    url(r'^chat2/$', views.ChatterBotAppView.as_view(), name='main'),
    url(r'^api/chatterbot/', views.ChatterBotApiView.as_view(), name='chatterbot'),
    #path('', views.chat, name='chat2'),
    #path('<str:room_name>/', views.room, name='room'),
    url('^spotify/?$', views.SpotifyBotView.as_view(), name='spotify'),
    url('^politica', views.ChatterBotAppView.as_view(), name='politica')
]
