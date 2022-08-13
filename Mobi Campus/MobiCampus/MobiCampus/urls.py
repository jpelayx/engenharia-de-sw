from unittest import result
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:usuario_login>/', views.detail, name='detail'),
    path('<str:usuario_login>/motorista/', views.motorista, name='motorista'),
    path('<str:usuario_login>/buscando_viagem/', views.buscando_viagem, name='viagem'),
    path('<str:usuario_login>/buscando_viagem/<str:busca>', views.resultado, name='resultado'),
]