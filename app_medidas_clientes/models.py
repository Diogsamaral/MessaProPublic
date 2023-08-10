from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="O número de telefone deve estar no formato: '+999999999'."
    )
    contato = models.CharField(validators=[telefone_regex], max_length=16)
    empresa = models.CharField(max_length=110)
    ombro_ombro = models.IntegerField()
    torax_busto = models.IntegerField()
    cintura_alta = models.IntegerField()
    cintura_baixa = models.IntegerField()
    quadril = models.IntegerField()
    altura_corpo = models.IntegerField()
    comp_camisa = models.IntegerField()
    comp_blazer = models.IntegerField()
    comp_vestido = models.IntegerField()
    comp_manga_curta = models.IntegerField()
    comp_manga_longa = models.IntegerField()
    larg_braco = models.IntegerField()
    punho = models.IntegerField()
    larg_perna = models.IntegerField()
    comp_saia = models.IntegerField()
    comp_calca = models.IntegerField()


class Tecido(models.Model):
    artigo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    fornecedor = models.CharField(max_length=100, blank=True)
    cliente = models.CharField(max_length=100, blank=True)
    metragem = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.artigo

