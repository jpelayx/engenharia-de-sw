from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Usuario, Administrador, Motorista
from django.template import loader
from django.http import Http404

def index(request):
    user_list = Usuario.objects.order_by('-nome')
    template = loader.get_template('MobiCampus/index.html')
    context ={
        'user_list': user_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, usuario_login):
    user=get_object_or_404(Usuario, pk=usuario_login)
    
    template = loader.get_template('MobiCampus/detail.html')
    contexto={
        'user':user,
    }

    return HttpResponse(template.render(contexto, request))

def results(request, usuario_login):
    resposta= "Voce esta olhando para o nome do usuario %s"
    return HttpResponse(resposta % usuario_login)

def verificar(request, usuario_login):
    return HttpResponse("Voce esta verificando o usuario %s" % usuario_login)