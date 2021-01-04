from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
    Marca
)

from .forms import (
    PessoaForm,
    MarcasForm,
    VeiculoForm,
    RotativoForm,
    MesalistaForm,
    MomMensalistaForm,
)


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


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/pessoa_update.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'pessoa': pessoa})


def lista_marcas(request):
    marcas = Marca.objects.all()
    form = MarcasForm()
    data = {'marcas': marcas, 'form': form}
    return render(request, 'core/lista_marcas.html', data)


def marcas_novo(request):
    form = MarcasForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_marcas')


def marcas_update(request, id):
    data = {}
    marcas = Marca.objects.get(id=id)
    form = MarcasForm(request.POST or None, instance=marcas)
    data['marcas'] = marcas
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_marcas')
    else:
        return render(request, 'core/marca_update.html', data)


def marcas_delete(request, id):
    marcas = Marca.objects.get(id=id)
    if request.method == 'POST':
        marcas.delete()
        return redirect('core_lista_marcas')
    else:
        return render(request, 'core/marcas_delete_confirm.html',
                      {'marcas': marcas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    return render(request, 'core/lista_veiculos.html',
                  {'veiculos': veiculos, 'form': form})


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/veiculo_update.html', data)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/veiculo_delete_confirm.html',
                      {'veiculo': veiculo})


def lista_movrotativos(request):
    movimento = MovRotativo.objects.all()
    form = RotativoForm()
    return render(request, 'core/lista_movrotativos.html',
                  {'movimento': movimento, 'form': form})


def rotativo_novo(request):
    form = RotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativo')


def rotativo_update(request, id):
    data = {}
    movimento = MovRotativo.objects.get(id=id)
    form = RotativoForm(request.POST or None, instance=movimento)
    data['movimento'] = movimento
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativo')
    else:
        return render(request, 'core/rotativo_update.html', data)


def rotativo_delete(request, id):
    movimento = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        movimento.delete()
        return redirect('core_lista_movrotativo')
    else:
        return render(request, 'core/movimento_delete_confirm.html',
                      {'movimento': movimento})


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MesalistaForm()
    return render(request, 'core/lista_mensalistas.html',
                  {'mensalistas': mensalistas, 'form': form})


def mensalista_novo(request):
    form = MesalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


def mensalista_update(request, id):
    data = {}
    mensalistas = Mensalista.objects.get(id=id)
    form = MesalistaForm(request.POST or None, instance=mensalistas)
    data['mensalistas'] = mensalistas
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/mensalista_update.html', data)


def mensalista_delete(request, id):
    mensalistas = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalistas.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/mensalista_delete_confirm.html',
                      {'mensalistas': mensalistas})


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


def mov_mes_update(request, id):
    data = {}
    mov_mensal = MovMensalista.objects.get(id=id)
    form = MomMensalistaForm(request.POST or None, instance=mov_mensal)
    data['mov_mensal'] = mov_mensal
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_mensal')
    else:
        return render(request, 'core/mov_mensal_update.html', data)


def mov_mes_delete(request, id):
    mov_mensal = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov_mensal.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/mov_mensal_del_confirm.html',
                      {'mov_mensal': mov_mensal})
