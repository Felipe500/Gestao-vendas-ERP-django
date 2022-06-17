from django.urls import path
from .views import (
    DashboardView, PagamentoView, PagamentoView2,NovoPedido,
    ListaVendas, NovoItemPedido,EditPedido,
    DeleteItemPedido,DeletePedido,EditItemPedido,
    filtra_produtos, add_item_ajax)


urlpatterns = [
    path('', ListaVendas.as_view(), name='lista-vendas'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('novo-pedido/', NovoPedido.as_view(), name="novo-pedido"),
    path('edit-pedido/<int:venda>/', EditPedido.as_view(), name="edit-pedido"),
    path('novo-item-pedido/<int:venda>/', NovoItemPedido.as_view(), name="novo-item-pedido"),
    path('delete-item-pedido/<int:item>/', DeleteItemPedido.as_view(), name="delete-item-pedido"),
    path('edit-item-pedido/<int:item>/', EditItemPedido.as_view(), name="edit-item-pedido"),
    path('delete-pedido/<int:venda>/', DeletePedido.as_view(), name="delete-pedido"),

    path('pagamento/<int:venda>/', PagamentoView.as_view(), name="pagamento"),
    path('pagamento2/<int:venda>/', PagamentoView2.as_view(), name="pagamento2"),
    path('add_item_list', add_item_ajax, name='add_item_list'),
    path('/filtra-produtos/', filtra_produtos, name='filtra_produtos'),


]