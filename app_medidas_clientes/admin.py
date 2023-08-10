from django.contrib import admin
from .models import Pessoa, Tecido

# Registre o modelo Pessoa para que ele apareça no admin do Django
admin.site.register(Pessoa)


class TecidoAdmin(admin.ModelAdmin):
    list_display = ['artigo', 'cor', 'fornecedor', 'cliente', 'metragem']

# Registre o modelo Tecido com a classe de admin personalizada
admin.site.register(Tecido, TecidoAdmin)
