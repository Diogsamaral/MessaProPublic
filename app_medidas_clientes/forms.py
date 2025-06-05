from django import forms
from .models import Tecido, Aviamento, Cliente

class TecidoForm(forms.ModelForm):
    class Meta:
        model = Tecido
        fields = ['artigo', 'cor', 'fornecedor', 'cliente', 'metragem']

class AviamentoForm(forms.ModelForm):
    class Meta:
        model = Aviamento
        fields = ['artigo', 'cor', 'fornecedor', 'cliente', 'quantidade']



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
        }
