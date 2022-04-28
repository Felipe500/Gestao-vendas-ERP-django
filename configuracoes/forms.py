from django import forms
from .models import Maq_cartao
from clientes.models import Cliente
from produtos.models import Produto, Categoria
from vendas.models import Descontos_Kits


class FormMaq_cartao(forms.ModelForm):
    class Meta:
        model = Maq_cartao
        fields = '__all__'

class FormMaq_cartao2(forms.ModelForm):

    nome = forms.CharField(required=True,label='Nome',
                                      widget=forms.TextInput(
                                          attrs={"class": "select form-control",
                                                 'name': 'descontos_list'}
                                      ))
    deb = forms.CharField(label='Débito',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type':"number",
                                        'step' : "0.01"}
                           ))
    cre1 = forms.CharField(label='Crédito X1',
                          widget=forms.NumberInput(
                              attrs={"class": "form-control",
                                     'name': 'descontos_list',
                                     'type': "number",
                                     'step': "0.01"}
                          ))
    cre2 = forms.CharField(label='Crédito X2',
                          widget=forms.NumberInput(
                              attrs={"class": "form-control",
                                     'name': 'descontos_list',
                                     'type': "number",
                                     'step': "0.01"}
                          ))
    cre3 = forms.CharField(label='Crédito X3',
                          widget=forms.NumberInput(
                              attrs={"class": "form-control",
                                     'name': 'descontos_list',
                                     'type': "number",
                                     'step': "0.01"}
                          ))
    cre4 = forms.CharField(label='Crédito X4',
                          widget=forms.NumberInput(
                              attrs={"class": "form-control",
                                     'name': 'descontos_list',
                                     'type': "number",
                                     'step': "0.01"}
                          ))
    cre5 = forms.CharField(label='Crédito X5',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre6 = forms.CharField(label='Crédito X6',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre7 = forms.CharField(label='Crédito X7',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre8 = forms.CharField(label='Crédito X8',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre9 = forms.CharField(label='Crédito X9',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre10 = forms.CharField(label='Crédito X10',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre11 = forms.CharField(label='Crédito X11',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))
    cre12 = forms.CharField(label='Crédito X12',
                           widget=forms.NumberInput(
                               attrs={"class": "form-control",
                                      'name': 'descontos_list',
                                      'type': "number",
                                      'step': "0.01"}
                           ))


    class Meta:
        model = Maq_cartao
        fields ='__all__'









