from django.urls import path

from .views import MovimentacoesView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('minhas-movimentacoes', MovimentacoesView.as_view(), name="home"),

]
