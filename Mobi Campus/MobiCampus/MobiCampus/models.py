from pyexpat import model
from django.db import models

max_passageiros=4
max_tam_string=50
max_tam_senha=20
tam_cnh=11
max_rota=300

# Create your models here.
class Usuario(models.Model):
    numeros= ((1, '1'), (2,'2'), (3,'3'), (4,'4'), (5, '5'))
    login=models.CharField(max_length=max_tam_string, primary_key=True)
    nome=models.CharField(max_length=max_tam_string)
    validado=models.BooleanField(default=False)
    aval=models.SmallIntegerField(default=5, choices=numeros)
    senha=models.CharField(max_length=max_tam_senha)
    
    def __str__(self):
        return self.nome

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
    finalizada=models.BooleanField(default=False)
    passageiros=models.SmallIntegerField(default=0)





