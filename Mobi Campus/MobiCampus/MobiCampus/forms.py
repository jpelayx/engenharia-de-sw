from django import forms

class Autenticacao(forms.Form):
    login=forms.CharField(label='Login', max_length=50)
    senha=forms.CharField(label='Senha', max_length=20)

class Pedido(forms.Form):
    origem=forms.CharField(label='Origem', max_length=50)
    destino=forms.CharField(label='Destino', max_length=50)
