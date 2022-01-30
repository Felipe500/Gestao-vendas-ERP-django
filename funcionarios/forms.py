from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['user', 'nome', 'sobrenome', 'data_nasc', 'celular', 'email','cep','endereco']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

