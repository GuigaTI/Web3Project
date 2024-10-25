from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    duracao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10,decimal_places=2)