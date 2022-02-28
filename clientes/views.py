from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Cliente
from .forms import ClienteForm
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from  .decorador import *



@login_required
@allowed_users(allowed_roles=['cliente','admin'])
def clientes_list(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)


    if nome or sobrenome:
        cliente = Cliente.objects.using('default').filter(nome__icontains=nome, sobrenome__icontains=sobrenome)
    else:
        cliente = Cliente.objects.using('default').all()

    footer_message = "Desenvolvido com Django 3.2"
    return render(request, 'clientes.html', {'clientes': cliente, 'footer_message':footer_message})


@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.add_person'):
        return HttpResponse('Nao autorizado')
    elif not request.user.is_superuser:
        return HttpResponse('Nao e superusuario')
    form = ClienteForm(request.POST or None, request.FILES or None)
    footer_message = "Desenvolvido com Django 3.2"


    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('person_list')
    return render(request, 'cliente_form.html', {'form': form, 'footer_message':footer_message})


@login_required
def persons_update(request, id):
    #person = get_object_or_404(Person, pk=id)
    cliente = Cliente.objects.using('default').get(id=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if form.is_valid():
        form = form.save(commit=False)
        form.save()

        return redirect('person_list')

    return render(request, 'cliente_form.html', {'form': form})



def persons_delete(request, id):
    cliente = Cliente.objects.using('default').get(id=id)

    if request.method == 'POST':
        Cliente.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'cliente': cliente})



class PersonList(LoginRequiredMixin, ListView):
    model = Cliente

    @method_decorator(allowed_users(['admin12']), name='dispatch')
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        primeiro_acesso = self.request.session.get('primeiro_acesso', False)

        if not primeiro_acesso:
            context['message'] = 'Seja bem vindo ao seu primeiro acesso hoje'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'Voce ja acessou hoje'

        return context


class PersonDetail( DetailView):
    model = Cliente

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Cliente.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()

        return context

class PersonCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'

class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')

class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('clientes.deletar_clientes',)

    model = Cliente
    #success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('person_list_cbv')


