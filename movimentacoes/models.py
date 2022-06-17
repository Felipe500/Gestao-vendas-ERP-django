from django.db import models
from common import choices
from django.contrib.auth import get_user_model

User = get_user_model()


class Movimentacoes(models.Model):
    tipo = models.CharField(max_length=50, choices=choices.STATUS_VENDA, verbose_name='TIPO')
    id_moviemnto = models.PositiveSmallIntegerField(max_length=1, blank=True, null=True)
    movimento = models.CharField(max_length=35)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Vendendor')
    forma_pg = models.CharField(max_length=50, choices=choices.FORMA_PG, verbose_name='Forma de pagamento')

    val_cartao = models.DecimalField(max_digits=6, decimal_places=2)
    val_cartao_liq = models.DecimalField(max_digits=6, decimal_places=2)
    val_pix = models.DecimalField(max_digits=6, decimal_places=2)
    val_transferencia = models.DecimalField(max_digits=6, decimal_places=2)
    val_especie = models.DecimalField(max_digits=6, decimal_places=2)
    val_total = models.DecimalField(max_digits=6, decimal_places=2)

    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'

    def __str__(self) -> str:
        return str(self.id_moviemnto + ' - '+self.movimento)

    @property
    def minhas_entradas(self):
        total_entradas = self.objects.filter(tipo=choices.ENTRADA).aggregate(sum('valor'))['valor__sum'] or 0.00
        return total_entradas

    @property
    def minhas_saidas(self):
        total_saidas = self.objects.filter(tipo=choices.SAIDA).aggregate(sum('valor'))['valor__sum'] or 0.00
        return total_saidas

