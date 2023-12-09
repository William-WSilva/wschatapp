from django.contrib import admin
from apps.wschatapp.models import Post, Comentario, Curtida, Rede, PostSalvo, UsuarioInfo

@admin.register(UsuarioInfo)
class UsuarioInfoAdmin(admin.ModelAdmin):
    list_display = ('id','usuario', 'foto_perfil')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','usuario', 'data_hora', 'descricao', 'imagem')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id','usuario', 'post', 'comentario', 'data_hora')

@admin.register(Curtida)
class CurtidaAdmin(admin.ModelAdmin):
    list_display = ('id','usuario', 'post')

@admin.register(Rede)
class RedeAdmin(admin.ModelAdmin):
    list_display = ('id','usuario', 'seguido')

@admin.register(PostSalvo)
class PostSalvoAdmin(admin.ModelAdmin):
    list_display = ('id','usuario', 'post')
