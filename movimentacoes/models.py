from django.db import models



# Create your models here.
class Movimentacoes(models.Model):
    tipo = models.CharField(max_length=100)
    movimento = models.DecimalField(max_digits=5, decimal_places=2)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.DecimalField(max_digits=5, decimal_places=2)
    forma_pg = models.DecimalField(max_digits=5, decimal_places=2)
    val_cartao = models.DecimalField(max_digits=5, decimal_places=2)
    val_cartao_liq = models.DecimalField(max_digits=5, decimal_places=2)
    val_pix = models.DecimalField(max_digits=5, decimal_places=2)
    val_transferencia = models.DecimalField(max_digits=5, decimal_places=2)
    val_especie = models.DecimalField(max_digits=5, decimal_places=2)
    val_total = models.DecimalField(max_digits=5, decimal_places=2)
    id_moviemnto = models.DecimalField(max_digits=5, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)


