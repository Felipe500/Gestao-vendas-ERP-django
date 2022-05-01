from django.shortcuts import render
from django.views.generic.base import TemplateView

class MovimentacoesView(TemplateView):
    template_name = 'movimentacoes/movimentacoes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Ola, seja bem vindo ao curso de Django advanced'
        return context
