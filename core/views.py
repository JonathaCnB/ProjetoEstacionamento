from django.shortcuts import render
# from django.http import HttpResponse
from .models import Pessoa, Veiculo, MovRotativo, MovMensalista


def home(request):
    context = {'mensagem': 'Ola mundo'}
    # return render(request, 'core/index.html', context) essa opção não requer configuração do arquivo setting
    # Apenas criar na pasta da app uma pasta /template/nomadaApp/
    return render(request, 'base.html', context) # Essa opção esta puxando essa aquivo da pasta raiz chamada template
    # Porem precisa ser configurado no settins


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    return render(request, 'core/lista_movrotativos.html',
                  {'mov_rotativos': mov_rotativos})


def lista_mensalista(request):
    mensalista = MovMensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalista': mensalista})
