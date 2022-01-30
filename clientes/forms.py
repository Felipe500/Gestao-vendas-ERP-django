from django.forms import ModelForm
from .models import Cliente
from funcionarios.models import Funcionario

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

