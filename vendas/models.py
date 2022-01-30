from django.db import models
from django.db.models.signals import post_save, m2m_changed, pre_save, post_delete
from django.db.models import Sum, F, FloatField, Max, IntegerField
from django.dispatch import receiver
from clientes.models import Cliente
from produtos.models import Produto, Estoque
from funcionarios.models import Funcionario
from .managers import VendaManager
from django.contrib.auth import get_user_model
User = get_user_model()

class VendaStatus(models.TextChoices):

    ABERTA = 'AB', 'Aberta'
    FECHADA = 'FE', 'Fechada'
    PROCESSANDO = 'PR', 'Processando'
    DESCONHECIDO = 'DC', 'Desconhecido'



class Venda(models.Model):

    valor = models.DecimalField(max_digits=5, decimal_places=2,  null=True, blank=True, default=0)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    nfe_emitida = models.BooleanField(default=False)
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

    def calcular_total(self):
        tot = self.itemsvenda_set.all().aggregate(
            tot_ped=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['tot_ped'] or 0
        tot = tot - float(self.impostos) - float(self.desconto)
        self.valor = tot
        Venda.objects.filter(id=self.id).update(valor=tot)
        #tot = 0
        #for produto in self.produtos.all():
            #tot += produto.preco
        #return (tot - self.desconto) - self.impostos

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
        print('anterior qted: ', str(self.quantidade))
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

    def dados_anteriores(self):
        #print('produto q: ',self.produto.qted)
        #print(self.produto)
        #print('atual qted produto: ',self.quantidade)
        #self.produto.qted += 1
        #('antes estoque alterado--------------------------')
        #self.produto.save()
        pass

    def Recupera_Qted_anterior(self):
        #print(self.Qted_anterior)
        if self.Qted_anterior != self.quantidade:
            self.Qted_anterior = self.quantidade
            print(self.Qted_anterior)



    def __str__(self):
        return str(self.venda) + ' - ' + self.produto.descricao



#@receiver(post_init, sender=ItemsVenda)
#def Alteracao_estoque(sender, instance, **kwargs):
#    instance.Recupera_Qted_anterior()


@receiver(post_delete, sender=ItemsVenda)
def Atualizar_Itens_Venda_del(sender, instance, **kwargs):
    instance.venda.calcular_total()

@receiver(post_save, sender=ItemsVenda)
def Atualizar_Itens_Venda(sender, instance, **kwargs):
    instance.venda.calcular_total()

    

@receiver(post_save, sender=Venda)
def Atualizar_Venda(sender, instance, **kwargs):
    instance.calcular_total()