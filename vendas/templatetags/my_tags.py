from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return datetime.now().strftime(format_string)


@register.simple_tag
def footer_message():
    return 'Desenvolvimento web com Django 2.0.2'

@register.simple_tag
def cabecalho_1():
    return 'NOVA VENDA'

@register.simple_tag
def cabecalho_2():
    return 'DETALHES DA VENDA'

@register.simple_tag
def text_bt_cabecalho1():
    return 'CRIAR VENDA'

@register.simple_tag
def text_bt_cabecalho2():
    return 'ATUALIZAR CABEÇALHO DA VENDA'

