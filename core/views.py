from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    context = {'mensagem': 'Ola mundo'}
    # return render(request, 'core/index.html', context) essa opção não requer configuração do arquivo setting
    # Apenas criar na pasta da app uma pasta /template/nomadaApp/
    return render(request, 'base.html', context) # Essa opção esta puxando essa aquivo da pasta raiz chamada template
    # Porem precisa ser configurado no settins

