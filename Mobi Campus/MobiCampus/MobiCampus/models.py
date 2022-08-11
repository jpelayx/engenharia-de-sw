from django.db import models

max_passageiros=4
max_tam_string=50
tam_cnh=11
max_rota=max_tam_string*3

# Create your models here.
class Usuario(models.Model):
    login=models.CharField(max_length=max_tam_string, primary_key=True)
    nome=models.CharField(max_length=max_tam_string)
    validado=models.BooleanField(default=False)
    aval=models.IntegerField(default=5)
    
    def __str__(self):
        return self.login

class Administrador(Usuario):
    permissao=models.BooleanField()

    def __str__(self):
        return super().__str__()

class Motorista(Usuario):
    cnh=models.CharField(max_length=tam_cnh)

    def __str__(self):
        return super().__str__()

class Carona(Motorista):
    origem=models.CharField(max_length=max_tam_string)
    destino=models.CharField(max_length=max_tam_string)
    rota=models.CharField(max_length=max_rota)
    custo=models.IntegerField()
    fializada=models.BooleanField(default=False)


