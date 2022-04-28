from django.db import models

class Maq_cartao(models.Model):
    nome = models.CharField(max_length=40, blank=True)
    deb = models.CharField(max_length=2,null=True, blank=True)
    cre1 = models.CharField(max_length=2, null=True, blank=True)
    cre2 = models.CharField(max_length=2, null=True, blank=True)
    cre3 = models.CharField(max_length=2, null=True, blank=True)
    cre4 = models.CharField(max_length=2, null=True, blank=True)
    cre5 = models.CharField(max_length=2, null=True, blank=True)
    cre6 = models.CharField(max_length=2, null=True, blank=True)
    cre7 = models.CharField(max_length=2, null=True, blank=True)
    cre8 = models.CharField(max_length=2, null=True, blank=True)
    cre9 = models.CharField(max_length=2, null=True, blank=True)
    cre10 = models.CharField(max_length=2, null=True, blank=True)
    cre11 = models.CharField(max_length=2, null=True, blank=True)
    cre12 = models.CharField(max_length=2, null=True, blank=True)


    def __str__(self):
        return self.nome