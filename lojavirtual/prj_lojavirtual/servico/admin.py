from django.contrib import admin
from .models import PrestadorServico, Servico

@admin.register(PrestadorServico)
class PrestadorServicoAdmin(admin.ModelAdmin):
    list_display = ['empresa', 'contato', 'telefone', 'slug']
    list_filter = ['data_criacao', 'contato']
    prepopulated_fields = {'slug': ('empresa',)}  # Slug gerado automaticamente com base no nome da empresa
    search_fields = ['empresa', 'contato']  # Campo de busca no admin

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'valor', 'prestador_servico', 'slug']
    list_filter = ['nome']
    list_editable = ['valor']  # Permite editar o valor direto na lista
    prepopulated_fields = {'slug': ('nome',)}  # Slug automático com base no nome
    search_fields = ['nome', 'descricao']  # Campo de busca no admin
