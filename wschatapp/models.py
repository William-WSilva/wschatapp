from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relacionamento um para um com o modelo User padrão
    nome = models.CharField(max_length=100, null=False, blank=False)  # Campo para o nome do usuário
    sobrenome = models.CharField(max_length=100, null=False, blank=False)  # Campo para o sobrenome do usuário
    email = models.EmailField(null=False, blank=False)  # Campo para o email do usuário

    def __str__(self):
        return self.user.username  # Retorna o nome de usuário do modelo User

# Definição do modelo para os Posts
class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Chave estrangeira para o usuário
    data_hora = models.DateTimeField(auto_now_add=True)  # Data e hora do post
    descricao = models.TextField(null=False, blank=False)  # Descrição do post
    imagem = models.ImageField(upload_to='images/')  # Campo para imagem do post

# Definição do modelo para os Comentários
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Chave estrangeira para o usuário
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Chave estrangeira para o post relacionado
    comentario = models.TextField(null=False, blank=False)  # Texto do comentário
    data_hora = models.DateTimeField(auto_now_add=True)  # Data e hora do comentário

# Definição do modelo para as Curtidas
class Curtida(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Chave estrangeira para o usuário
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Chave estrangeira para o post curtido

# Definição do modelo para a Rede de Seguidores
class Rede(models.Model):
    usuario = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)  # Chave estrangeira para o usuário
    seguido = models.ForeignKey(User, related_name='seguido', on_delete=models.CASCADE)  # Chave estrangeira para o usuário seguido
    seguidor = models.ForeignKey(User, related_name='seguidor', on_delete=models.CASCADE)  # Chave estrangeira para o seguidor

# Definição do modelo para os Posts Salvos
class PostSalvo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Chave estrangeira para o usuário
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Chave estrangeira para o post salvo