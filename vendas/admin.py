from django.contrib import admin
from .models import Venda
from .models import ItemsVenda
from .actions import nfe_emitida, nfe_nao_emitida
# Register your models here.
class ItensVendasInline(admin.TabularInline):
    model = ItemsVenda
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    #autocomplete_fields = ("pessoa",)

    list_display = ('pk', 'cliente', 'vendedor','nfe_emitida','valor')
    #search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    inlines = [ItensVendasInline]


    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'

admin.site.register(Venda,VendaAdmin)
admin.site.register(ItemsVenda)