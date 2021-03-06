from django.urls import path
from .views import (
    index,
    home,
    lista_pessoas,
    lista_marcas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalista,
    lista_mov_mensal,
    pessoa_novo,
    marcas_novo,
    veiculo_novo,
    rotativo_novo,
    mensalista_novo,
    mov_mensal_novo,
    pessoa_update,
    marcas_update,
    veiculo_update,
    rotativo_update,
    mensalista_update,
    mov_mes_update,
    pessoa_delete,
    marcas_delete,
    veiculo_delete,
    rotativo_delete,
    mensalista_delete,
    mov_mes_delete,
)


urlpatterns = [
    path('', index, name='core_index'),
    path('core/index.html', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>/', pessoa_delete, name='core_pessoa_delete'),

    path('marcas/', lista_marcas, name='core_lista_marcas'),
    path('marcas-novo/', marcas_novo, name='core_marcas_novo'),
    path('marcas-update/<int:id>/', marcas_update, name='core_marcas_update'),
    path('marcas-delete/<int:id>/', marcas_delete, name='core_marcas_delete'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<int:id>/',
         veiculo_update, name='core_veiculo_update'),
    path('veiculo-delete/<int:id>/',
         veiculo_delete, name='core_veiculo_delete'),

    path('mov-rotativo/', lista_movrotativos, name='core_lista_movrotativo'),
    path('mov-novo/', rotativo_novo, name='core_rotativo_novo'),
    path('mov-update/<int:id>/', rotativo_update, name='core_rotativo_update'),
    path('rotativo-delete/<int:id>/',
         rotativo_delete, name='core_rotativo_delete'),

    path('mensalista/', lista_mensalista, name='core_lista_mensalista'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista-novo'),
    path('mensalista-update/<int:id>/',
         mensalista_update, name='core_mensalista_update'),
    path('mensalista-delete/<int:id>/',
         mensalista_delete, name='core_mensalista_delete'),

    path('mov-mensal/', lista_mov_mensal, name='core_lista_mov_mensal'),
    path('mov-mensal-novo/', mov_mensal_novo, name='core_mov_mensal_novo'),
    path('mov-mensal-update/<int:id>/',
         mov_mes_update, name='core_mov_mensal_update'),
    path('mov-mensal-delete/<int:id>/',
         mov_mes_delete, name='core_mov_mensal_delete'),

]
