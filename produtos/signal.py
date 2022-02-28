from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Estoque,Produto


def create_estoque_produto(sender, instance, created, **kwargs):
    print('perfil criado com sucesso!')
    if created:
        #Produto_Estoque = Estoque(produto_id=instance.pk, estoque_atual=0)
        Estoque.objects.create(
            produto_id=instance.pk,
            estoque_atual=0
        )
        print('Estoque para o produto criado com sucesso!')

post_save.connect(create_estoque_produto, sender=Produto)
