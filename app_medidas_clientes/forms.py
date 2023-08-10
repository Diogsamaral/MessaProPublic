from django import forms
from .models import Tecido

class TecidoForm(forms.ModelForm):
    class Meta:
        model = Tecido
        fields = ['artigo', 'cor', 'fornecedor', 'cliente', 'metragem']
