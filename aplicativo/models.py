from django.db import models
import uuid


def rename_image(instance, filename):
    ext = filename.split('.')[-1]  # Obtém a extensão do arquivo
    # Gera um nome único para o arquivo com base em UUID e adiciona a extensão
    return f'imagens/courses/{uuid.uuid4()}.{ext}'
# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='imagens/users/', null=True)

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    duracao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='imagens/courses/', null=True)  # Somente esta linha



class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/', null=True)