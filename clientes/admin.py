from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields': ('nome', 'sobrenome', 'email','celular','data_nasc')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('endereco', 'cep')
        })
    )
    # fields = (('doc', 'first_name'), 'last_name', ('age', 'salary'), 'bio', 'photo')
    # exclude = ('bio', )
    #list_filter = ('age', 'salary')
    list_display = ('nome', 'sobrenome', 'email', 'celular')
    search_fields = ('nome', 'sobrenome')
    #autocomplete_fields = ['nome']







admin.site.register(Cliente, ClienteAdmin)

