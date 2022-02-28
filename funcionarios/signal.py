from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Funcionario


def funcionario_profile(sender, instance, created, **kwargs):
    print('perfil criado com sucesso!')
    if created:
        if not Group.objects.filter(name='funcionario').exists():
            print("criado grupo funcionario")
            Group.objects.create(name='funcionario')

        group = Group.objects.get(name='funcionario')
        instance.groups.add(group)
        Funcionario.objects.create(
            user=instance,
            nome=instance.username,
            sobrenome='*',
        )
        print('perfil criado com sucesso!')

post_save.connect(funcionario_profile, sender=User)
