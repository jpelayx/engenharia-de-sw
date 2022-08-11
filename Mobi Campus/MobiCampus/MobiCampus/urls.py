from unittest import result
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:usuario_login>/', views.detail, name='detail'),
    path('<str:usuario_login>/results/', views.results, name='results'),
    path('<str:usuario_login>/verificar/', views.verificar, name='verificar'),
]