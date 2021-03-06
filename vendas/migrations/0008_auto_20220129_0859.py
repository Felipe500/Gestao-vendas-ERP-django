# Generated by Django 3.2.9 on 2022-01-29 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0013_cliente_vendedor_cadastro'),
        ('funcionarios', '0001_initial'),
        ('vendas', '0007_auto_20220124_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='numero',
        ),
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='funcionarios.funcionario'),
        ),
    ]
