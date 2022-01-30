from django.db import models
from django.core.mail import send_mail, mail_admins, send_mass_mail
from django.template.loader import render_to_string
from django.utils.text import slugify
from django.contrib.auth import get_user_model
#updates
#from django_resized import ResizedImageField

User = get_user_model()


class Funcionario(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=40, blank=True)
    sobrenome = models.CharField(max_length=40, blank=True,null=True)
    data_nasc = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    celular = models.CharField(max_length=15,null=True, blank=True)
    email = models.CharField(max_length=50,null=True, blank=True)
    cep = models.CharField(max_length=15,null=True, blank=True)
    endereco = models.CharField(max_length=50,null=True, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True, null=True)
    data_cadastro  = models.DateTimeField(auto_now_add=True)

    @property
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def __str__(self):
        return self.nome + '-' + self.sobrenome
