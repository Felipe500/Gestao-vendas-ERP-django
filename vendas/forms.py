from django import forms
from .models import ItemsVenda, Venda
from clientes.models import Cliente

class ItemPedidoForm(forms.Form):
    produto_id = forms.CharField(label='ID do Produto', max_length=100)
    quantidade = forms.IntegerField(label='Quantidade')
    desconto = forms.DecimalField(label='Desconto', max_digits=7, decimal_places=2)


class ItemForm(forms.ModelForm):

    class Meta:
        model = ItemsVenda
        fields = ['quantidade','desconto']

class VendaForm(forms.ModelForm):
   # cliente = forms.ModelChoiceField()
    #cliente = forms.ModelChoiceField(label='Cliente',
     #                                queryset=Cliente.objects.all(),
     #
     #                                widget=forms.Select(attrs={"class":"form-control",'name':'cliente'})
     #                                  )
    class Meta:
        model = Venda
        fields = ['id','cliente','desconto']

        widgets = {

            'cliente': forms.Select(attrs={"class": "form-control", 'name': 'cliente'}),
            'desconto': forms.NumberInput(attrs={"class": "form-control", 'name': 'desconto'})

        }
        localized_fields = ('id',)

