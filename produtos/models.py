import time
from django.utils.timezone import now
from django.db import models
from funcionarios.models import Funcionario
from django.db.models.signals import post_save, m2m_changed, pre_save, post_delete,pre_delete
from django.dispatch import receiver
from django.urls import reverse



class Categoria(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        print('USUARIO CRIADO COM SUCESSO', str(self.pk))
        if Estoque.objects.filter(produto_id=self.pk).exists():
            print("produto já criado no estoque...")
        else:
            Produto_Estoque = Estoque(produto_id=self.pk, estoque_atual=0)
            Produto_Estoque.save()
        super(Produto, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('produto_list')

    def __str__(self):
        return self.descricao


class Estoque(models.Model):
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.CASCADE)
    estoque_atual = models.DecimalField(max_digits=5, decimal_places=2)
    estoque_minimo = models.IntegerField(default=0)
    data_atualizacao = models.DateTimeField(default=now, editable=False)
    vendedor = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.CASCADE)


    def alterar_estoque(self,produto, qted):
        Novo_estoque = Estoque.objects.get(produto_id=produto)
        Novo_estoque.estoque_atual += qted
        Novo_estoque.save()
        print( 'produto alterado - ',Novo_estoque.estoque_atual)
        print('valor inserido - ', qted)

    def cria_estoque(self):
        pass

    def __str__(self):
        return str(self.produto.__str__())


