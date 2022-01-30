from django.urls import path
from .views import *


urlpatterns = [
    path('list/', produtos_list, name="produto_list"),
    path('estoque/', Estoque_produtos, name="estoque_produtos"),
    path('alterar_estoque/<int:id>/', Editar_Estoque, name="editar_estoque"),

    path('novo/', Produto_Novo, name="Produto_Novo"),
    path('update/<int:id>/', Produto_update, name="produto_update"),
    path('delete/<int:id>/', Produto_Delete, name="Produto_Delete"),
]