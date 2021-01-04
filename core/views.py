from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista


from .forms import PessoaForm


def home(request):
    context = {'mensagem': 'Ola mundo'}
    # return render(request, 'core/index.html', context) essa opção não requer configuração do arquivo setting
    # Apenas criar na pasta da app uma pasta /template/nomadaApp/
    return render(request, 'base.html', context) # Essa opção esta puxando essa aquivo da pasta raiz chamada template
    # Porem precisa ser configurado no settins


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    return render(request, 'core/lista_movrotativos.html',
                  {'mov_rotativos': mov_rotativos})


def lista_mensalista(request):
    mensalista = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html',
                  {'mensalista': mensalista})


def lista_mov_mensal(request):
    mov_mensal = MovMensalista.objects.all()
    return render(request, 'core/lista_mov_mensal.html',
                  {'mov_mensal': mov_mensal})
