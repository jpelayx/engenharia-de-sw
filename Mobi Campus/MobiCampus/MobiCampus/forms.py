from django import forms

class Autenticacao(forms.Form):
    login=forms.CharField(label='Login', max_length=50)
    senha=forms.CharField(label='Senha', max_length=20)
