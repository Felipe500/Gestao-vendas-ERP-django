# Generated by Django 3.2.9 on 2022-04-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maq_cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=40)),
                ('deb', models.CharField(blank=True, max_length=2, null=True)),
                ('cre1', models.CharField(blank=True, max_length=2, null=True)),
                ('cre2', models.CharField(blank=True, max_length=2, null=True)),
                ('cre3', models.CharField(blank=True, max_length=2, null=True)),
                ('cre4', models.CharField(blank=True, max_length=2, null=True)),
                ('cre5', models.CharField(blank=True, max_length=2, null=True)),
                ('cre6', models.CharField(blank=True, max_length=2, null=True)),
                ('cre7', models.CharField(blank=True, max_length=2, null=True)),
                ('cre8', models.CharField(blank=True, max_length=2, null=True)),
                ('cre9', models.CharField(blank=True, max_length=2, null=True)),
                ('cre10', models.CharField(blank=True, max_length=2, null=True)),
                ('cre11', models.CharField(blank=True, max_length=2, null=True)),
                ('cre12', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
    ]
