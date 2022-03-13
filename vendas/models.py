from django.db import models
from django.db.models.signals import post_save, m2m_changed, pre_save, post_delete,pre_delete
from django.db.models import Sum, F, FloatField, Max, IntegerField
from django.dispatch import receiver
from clientes.models import Cliente
from produtos.models import Produto, Estoque
from .managers import VendaManager
from django.contrib.auth import get_user_model

User = get_user_model()



class Descontos_Kits(models.Model):
    descricao = models.CharField(max_length=25)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return str(self.descricao) +' - R$ ' +str(self.valor)


class VendaStatus(models.TextChoices):

    ABERTA = 'AB', 'Aberta'
    FECHADA = 'FE', 'Fechada'
    PROCESSANDO = 'PR', 'Processando'
    DESCONHECIDO = 'DC', 'Desconhecido'




class Venda(models.Model):
    ABERTA = 'Aberta'
    FECHADA = 'Fechada'
    ORCAMENTO = 'Orçamento'
    DESCONHECIDO = 'Desconhecido'

    STATUS = (
        (ABERTA, ('Aguardando pagamento')),
        (ORCAMENTO, ('Em Orçamento')),
        (FECHADA, ('Pago')),
        (4, ('Cancelado')),
    )

    valor = models.DecimalField(max_digits=6, decimal_places=2,  null=True, blank=True, default=0)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    nfe_emitida = models.BooleanField(default=False)
    #Cancelado = models.BooleanField(default=False)
    status = models.CharField(
        choices=VendaStatus.choices,
        default=VendaStatus.DESCONHECIDO,
        max_length=7)

    objects = VendaManager()

    class Meta:
        permissions = (
            ('setar_nfe', 'Usuario pode alterar parametro NF-e'),
            ('ver_dashboard', 'Pode visualizar o Dashboard'),
            ('permissao3', 'Permissao 3'),
        )

    def save(self, *args, **kwargs):
        super(Venda, self).save(*args, **kwargs)

    def calcular_total(self):
        tot = self.itemsvenda_set.all().aggregate(
            tot_ped=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['tot_ped'] or 0
        tot = tot - float(self.impostos) - float(self.desconto)
        self.valor = tot
        Venda.objects.filter(id=self.id).update(valor=tot)

    def Reposicao_Estoque(self):
        itens = self.itemsvenda_set.all()
        for item in itens:
            print(item.quantidade)


    def __str__(self):
        return str(self.pk) + '- venda'


class ItemsVenda(models.Model):
    Qted_anterior = 0
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        verbose_name_plural = "Itens do pedido"
        unique_together = [['venda', 'produto']]

    def save(self, *args, **kwargs):
        print('USUARIO CRIADO COM SUCESSO', str(self.produto.pk))
        if Estoque.objects.filter(produto_id=self.produto.pk).exists():
            print("produto já criado no estoque...")
        else:
            Produto_Estoque = Estoque(produto=self.produto.pk, estoque_atual=0)
            Produto_Estoque.save()
        super(ItemsVenda, self).save(*args, **kwargs)

    def alterar_estoque(self):
        produto_estoque = Estoque.objects.get(produto=self.produto)
        print('em estoque-',produto_estoque.estoque_atual)
        produto_pedido = Produto.objects.get(id=int(self.produto.pk))
        Qted_estoque = int(self.quantidade) - int(self.Qted_anterior.id)
        produto_pedido.qted += Qted_estoque
        produto_pedido.save()
        print('data: ',self.Qted_anterior)
        print("data 2: ",Qted_estoque)


    def __str__(self):
        return str(self.venda) + ' - ' + self.produto.descricao




@receiver(post_delete, sender=ItemsVenda)
def Atualizar_Itens_Venda_del(sender, instance, **kwargs):
    instance.venda.calcular_total()

@receiver(post_save, sender=ItemsVenda)
def Atualizar_Itens_Venda(sender, instance, **kwargs):
    instance.venda.calcular_total()



@receiver(post_delete, sender=Venda)
def Alterar_estoque(sender, instance, **kwargs):
    instance.Reposicao_Estoque()

@receiver(post_save, sender=Venda)
def Atualizar_Venda(sender, instance, **kwargs):
    instance.calcular_total()