
from django import forms
from .models import Tecido, Aviamento, Cliente, Pessoa

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
        fields = [
            'nome',
            'email',
            'telefone',
            'endereco',
            'linkedin',
            'cnpj',
            'cpf',
            'inscricao_estadual',
            'inscricao_municipal',
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control'}),
            'inscricao_municipal': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'