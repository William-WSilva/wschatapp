from django.contrib import admin
from .models import UserProfile, Post, Comentario, Curtida, Rede, PostSalvo

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome', 'sobrenome', 'email')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_hora', 'descricao', 'imagem')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'post', 'comentario', 'data_hora')

@admin.register(Curtida)
class CurtidaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'post')

@admin.register(Rede)
class RedeAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'seguido', 'seguidor')

@admin.register(PostSalvo)
class PostSalvoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'post')
