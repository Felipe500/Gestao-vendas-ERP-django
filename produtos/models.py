import time
from django.utils.timezone import now
from django.db import models
from funcionarios.models import Funcionario


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    qted = models.IntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)

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

    def __str__(self):
        return str(self.produto.__str__())
