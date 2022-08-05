from django.db import models

# Create your models here.
#python manage.py makemigrations core

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)


class Empresa(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)


class Vaga(models.Model):
    nome = models.CharField(max_length=100)
    faixa_salarial = models.CharField(max_length=20)
    requisitos = models.CharField(max_length=100)
    escolaridade_min = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)




class Candidato_por_vaga(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato,on_delete=models.CASCADE)
    pretencao_salarial = models.CharField(max_length=20)
    experiencia = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=40)



