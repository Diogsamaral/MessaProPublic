from django.shortcuts import render, redirect
from .models import Pessoa, Tecido, Aviamento
from django.shortcuts import render, get_object_or_404
from .forms import TecidoForm, AviamentoForm, ClienteForm, PessoaForm
from django.urls import reverse



def buscar_pessoas(request):
    if 'query' in request.GET:
        query = request.GET['query']
        resultados = Pessoa.objects.filter(nome__icontains=query) | Pessoa.objects.filter(empresa__icontains=query)        
        aviamentos = Aviamento.objects.filter(artigo__icontains=query)
        tecidos = Tecido.objects.filter(artigo__icontains=query)
    else:
        resultados = None
        aviamentos = None
        tecidos = None

    return render(request, 'buscar.html', {'resultados': resultados, 'aviamentos': aviamentos, 'tecidos': tecidos})



def home(request):
    return render(request, 'home.html')



def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cadastro-pessoa')
        else:
            print(form.errors)  # DEBUG
    else:
        form = PessoaForm()

    return render(request, 'cadastrar-pessoa.html', {'form': form})

    


def exibir_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    return render(request, 'exibir_pessoa.html', {'pessoa': pessoa})



def todas_pessoas(request):
    # Consulta o banco de dados e obtém todos os registros do modelo MeuModelo
    todos_os_registros = Pessoa.objects.all()
    
    # Passe os registros para o template usando um dicionário
    context = {
        'registros': todos_os_registros,
    }
    
    # Renderiza o template com os dados e retorna a resposta HTTP
    return render(request, 'todas-pessoas.html', context)



def novo_tecido(request):
    if request.method == 'POST':
        form = TecidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('novo_tecido'))  # Redireciona para a URL nomeada 'novo_tecido'
    else:
        form = TecidoForm()
    return render(request, 'novo_tecido.html', {'form': form})


def novo_aviamento(request):
    if request.method == 'POST':
        form = AviamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('novo_aviamento'))  # Redireciona para a URL nomeada 'novo_tecido'
    else:
        form = AviamentoForm()
    return render(request, 'novo_aviamento.html', {'form': form})


def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastro.html', {'form': form})



def home(request):
    return render(request, 'app_medidas_clientes/home.html')
