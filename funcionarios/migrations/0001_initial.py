# Generated by Django 3.2.9 on 2022-01-24 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=40)),
                ('sobrenome', models.CharField(blank=True, max_length=40, null=True)),
                ('data_nasc', models.DateTimeField(auto_now_add=True, null=True)),
                ('celular', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('cep', models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, max_length=400, null=True, unique=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
