from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#python manage.py makemigrations core

class Candidato(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.user.first_name


class Empresa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=15)


    def __str__(self):
        return self.user.username



class Vaga(models.Model):
    nome = models.CharField(max_length=100)
    faixa_salarial = models.CharField(max_length=20)
    requisitos = models.CharField(max_length=400)
    escolaridade_min = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.nome




class Candidatura(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato,on_delete=models.CASCADE)
    pretencao_salarial = models.CharField(max_length=20)
    experiencia = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=40)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.candidato)



