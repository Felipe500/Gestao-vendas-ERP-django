from django import forms
from .models import Produto, Estoque


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        widgets = {

            'categoria': forms.Select(attrs={"class": "select", 'name': 'categoria'}),}




class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['produto','estoque_atual','estoque_minimo']

