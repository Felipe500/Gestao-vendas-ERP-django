# Generated by Django 3.2.9 on 2022-01-24 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_auto_20220124_1339'),
        ('vendas', '0007_auto_20220124_1339'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]