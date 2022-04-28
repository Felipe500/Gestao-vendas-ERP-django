from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from configuracoes.forms import FormMaq_cartao,FormMaq_cartao2
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Maq_cartao

@login_required()
def Settings(request):
    data = {}
    data['usuario'] = request.user
    return  render( request, "configuracoes/settings.html",data)

class Maq_cartaoList(LoginRequiredMixin,ListView):
    model = Maq_cartao
    #form_class = FormMaq_cartao2()
    template_name = 'configuracoes/settings.html'



class Maq_cartaoCreate(CreateView):
    model = Maq_cartao
    form_class = FormMaq_cartao2
    success_url = reverse_lazy('settings_app')
    template_name = 'configuracoes/settings_card_new.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Maq_cartao.objects.values('id', 'nome')
        return context

class Maq_cartaoUpdate(UpdateView):
    model = Maq_cartao
    form_class = FormMaq_cartao2
    success_url = reverse_lazy('settings_app')
    template_name = 'configuracoes/settings_card_update.html'

    def get_object(self, **kwargs):
        print(kwargs)
        texto = 'Atualizar produto'
        return Maq_cartao.objects.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Maq_cartao.objects.values('id', 'nome')
        return context

    def get_form_class(self):
        return FormMaq_cartao2

@login_required()
def Settings2(request):
    data = {}
    data['form1'] = FormMaq_cartao2()
    data['usuario'] = request.user
    return  render( request, "configuracoes/settings2.html",data)

def Cadastrar_Maq_Cartao(request):
    id_categoria = request.GET['outro_param']
    print(request.GET['outro_param'], 'ddd')

    categoria = Categoria.objects.get(id=id_categoria)

    qs_json = serializers.serialize('json', categoria.produto_set.all())
    return HttpResponse(qs_json, content_type='application/json')
