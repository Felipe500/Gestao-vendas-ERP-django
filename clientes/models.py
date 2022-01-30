from django.db import models
from django.core.mail import send_mail, mail_admins, send_mass_mail
from django.template.loader import render_to_string
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from funcionarios.models import Funcionario
from django.core.mail import send_mail, mail_admins, send_mass_mail
#updates
#from django_resized import ResizedImageField

User_funcionario = get_user_model()



class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30,null=True, blank=True)
    data_nasc = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    celular = models.CharField(max_length=15,null=True, blank=True)
    email = models.CharField(max_length=50,null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    cep = models.CharField(max_length=15,null=True, blank=True)
    endereco = models.CharField(max_length=50,null=True, blank=True)
    vendedor_cadastro = models.ForeignKey(User_funcionario, null=True, blank=True, on_delete=models.CASCADE)


    @property
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def save(self, *args, **kwargs):
        super(Cliente, self).save(*args, **kwargs)



    def __str__(self):
        return self.nome + ' ' + self.sobrenome






