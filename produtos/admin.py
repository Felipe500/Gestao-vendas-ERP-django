from django.contrib import admin
from  .models import Produto,  Estoque
# Register your models here.


class ProdutoAdmin(admin.ModelAdmin):

    #autocomplete_fields = ("pessoa",)

    list_display = ('id', 'descricao', 'preco', 'qted')
    #search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')

class EstoqueAdmin(admin.ModelAdmin):

    #autocomplete_fields = ("pessoa",)

    list_display = ('produto', 'estoque_atual', 'estoque_minimo')
    #search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')


admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Produto, ProdutoAdmin)