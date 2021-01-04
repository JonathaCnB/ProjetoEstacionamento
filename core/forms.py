from django.forms import ModelForm
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class RotativoForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'


class MesalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


class MomMensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'
