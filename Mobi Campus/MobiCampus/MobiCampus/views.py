from multiprocessing import context
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Usuario, Administrador, Motorista
from django.template import loader
from django.http import Http404
from .forms import Autenticacao

def index(request):
    if(request.method=='POST'):
        form=Autenticacao(request.POST)

        if(form.is_valid()):
            nome=form.cleaned_data['login']
            password=form.cleaned_data['senha']
            user=get_object_or_404(Usuario, pk=nome)

            if(user.senha==password):
                return HttpResponseRedirect(nome)
            else:
                error= loader.get_template('MobiCampus/index.html')
                contexto={
                    'form': form,
                    'erro': True,
                }
                return HttpResponse(error.render(contexto, request=request))
    

    else:
        form=Autenticacao()    
    
    template = loader.get_template('MobiCampus/index.html')
    contexto= {
        'form': form,
        'erro': False,
        }

    return HttpResponse(template.render(contexto, request))

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