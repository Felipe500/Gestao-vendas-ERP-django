from django.forms import ModelForm
from .models import Produto, Estoque


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class EstoqueForm(ModelForm):
    class Meta:
        model = Estoque
        fields = ['produto','estoque_atual','estoque_minimo']