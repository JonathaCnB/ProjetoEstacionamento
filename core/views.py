from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista


from .forms import PessoaForm, VeiculoForm, RotativoForm, MesalistaForm, MomMensalistaForm


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
    form = VeiculoForm()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos, 'form': form})


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def lista_movrotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    form = RotativoForm()
    return render(request, 'core/lista_movrotativos.html',
                  {'mov_rotativos': mov_rotativos, 'form': form})


def rotativo_novo(request):
    form = RotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativo')


def lista_mensalista(request):
    mensalista = Mensalista.objects.all()
    form = MesalistaForm()
    return render(request, 'core/lista_mensalistas.html',
                  {'mensalista': mensalista, 'form': form})


def mensalista_novo(request):
    form = MesalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


def lista_mov_mensal(request):
    mov_mensal = MovMensalista.objects.all()
    form = MomMensalistaForm()
    return render(request, 'core/lista_mov_mensal.html',
                  {'mov_mensal': mov_mensal, 'form': form})


def mov_mensal_novo(request):
    form = MomMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_mensal')
