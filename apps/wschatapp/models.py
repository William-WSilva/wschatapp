from django.contrib.auth.models import User
from django.db import models

class UsuarioInfo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='imagem/%Y/%m/%d/', blank=True)


# Definição do modelo para os Posts
class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Chave estrangeira para o usuário
    data_hora = models.DateTimeField(auto_now=True)  # Data e hora do post
    descricao = models.TextField(null=False, blank=False)  # Descrição do post
    imagem = models.ImageField(upload_to='imagem/%Y/%m/%d/', blank=True)  # Campo para imagem do post


# Definição do modelo para os Comentários
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Chave estrangeira para o usuário
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Chave estrangeira para o post relacionado
    comentario = models.TextField(null=False, blank=False)  # Texto do comentário
    data_hora = models.DateTimeField(auto_now=True)  # Data e hora do comentário


# Definição do modelo para as Curtidas
class Curtida(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Chave estrangeira para o usuário
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Chave estrangeira para o post curtido


# Definição do modelo para a Rede de Seguidores
class Rede(models.Model):
    usuario = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE, null=False, blank=False)  # Chave estrangeira para o usuário
    seguido = models.ForeignKey(User, related_name='seguido', on_delete=models.CASCADE, null=False, blank=False) # Chave estrangeira para o usuário seguido


# Definição do modelo para os Posts Salvos
class PostSalvo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Chave estrangeira para o usuário
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Chave estrangeira para o post salvo