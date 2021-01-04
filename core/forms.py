from django.forms import ModelForm
from .models import Pessoa, Marca, Veiculo, MovRotativo, Mensalista, MovMensalista


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class MarcasForm(ModelForm):
    class Meta:
        model = Marca
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
