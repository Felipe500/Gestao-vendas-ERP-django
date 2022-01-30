from django.urls import path
from .views import (
    DashboardView, NovoPedido,
    ListaVendas, NovoItemPedido,EditPedido,
    DeleteItemPedido,DeletePedido,EditItemPedido)


urlpatterns = [
    path('', ListaVendas.as_view(), name='lista-vendas'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('novo-pedido/', NovoPedido.as_view(), name="novo-pedido"),
    path('edit-pedido/<int:venda>/', EditPedido.as_view(), name="edit-pedido"),
    path('novo-item-pedido/<int:venda>/', NovoItemPedido.as_view(), name="novo-item-pedido"),
    path('delete-item-pedido/<int:item>/', DeleteItemPedido.as_view(), name="delete-item-pedido"),
    path('edit-item-pedido/<int:item>/', EditItemPedido.as_view(), name="edit-item-pedido"),
    path('delete-pedido/<int:venda>/', DeletePedido.as_view(), name="delete-pedido"),

]