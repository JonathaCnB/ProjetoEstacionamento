from django.contrib import admin
from .models import (
    Marca,
    Veiculo,
    Pessoa,
    Parametros,
    MovRotativo,
    Mensalista
)


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin', 'checkout', 'valor_hora', 'pago', 'total', 'horas_total',
        'veiculo')

    def veiculo(self, obj):
        return obj.veiculo


admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
