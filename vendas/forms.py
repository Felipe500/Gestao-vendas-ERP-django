from django import forms
from .models import ItemsVenda, Venda
from clientes.models import Cliente
from produtos.models import Produto, Categoria
from vendas.models import Descontos_Kits


class ProdutoCategoriaForm(forms.Form):
    categoria_list = forms.ModelChoiceField(queryset=Categoria.objects.all(),empty_label=None,
        label='CATEGORIA', widget=forms.Select(
        attrs={"class": "select form-control",
               'name': 'produto_list',
               'onchange': "filtra_produtos(this.value)"}
    ))

class ItemPedidoForm(forms.Form):
    produto_list = forms.ModelChoiceField(queryset=Produto.objects.all(), empty_label=None,label='Produtos',
        required=False,widget=forms.Select(
        attrs={"class": "select form-control",
               'name': 'cliente',
             }
    ))
    desconto = forms.ModelChoiceField(queryset=Descontos_Kits.objects.all(), to_field_name='valor',
                                      empty_label=None,
                                      label='Descontos para kits',
                                      widget=forms.Select(
                                          attrs={"class": "select form-control",
                                                 'name': 'descontos_list',
                                                 'id':  'desconto_produto'}
                                      ))

    quantidade = forms.IntegerField(label='Quantidade', initial=0)


class DescontoForm(forms.Form):
    desconto = forms.ModelChoiceField(queryset=Descontos_Kits.objects.all(), to_field_name= 'valor',empty_label=None, label='Descontos para kits',
                                            widget=forms.Select(
                                                attrs={"class": "select form-control",
                                                       'name': 'descontos_list',
                                                       }
                                            ))




class ItemForm(forms.ModelForm):
    desconto = forms.ModelChoiceField(queryset=Descontos_Kits.objects.all(),
                                      to_field_name='valor', empty_label=None,
                                      label='Descontos para kits',
                                      widget=forms.Select(
                                          attrs={"class": "select form-control",
                                                 'name': 'descontos_list'}
                                      ))
    class Meta:
        model = ItemsVenda
        fields = ['quantidade','desconto']

        widgets = {

            'quantidade': forms.NumberInput(attrs={"class": "form-control", 'name': 'cliente'}),
            'desconto': forms.NumberInput(attrs={"class": "form-control", 'name': 'desconto', 'id':  'desconto_produto'})
        }


class ProdutoAddForm(forms.ModelForm):
    #--------------------------------------
    class Meta:
        model = ItemsVenda
        fields = ['produto']
        widgets = {
            'produto': forms.Select(attrs={"class": "select form-control",
                                           'name': 'produto_list',
                                          }),
        }


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

