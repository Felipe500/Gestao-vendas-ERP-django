import datetime
import json

from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View

from produtos.models import Produto, Estoque
from .models import Venda, ItemsVenda, VendaStatus, Descontos_Kits
from django.db.models import Sum, F, FloatField, Min, Max, Avg
from .forms import VendaForm, ItemPedidoForm, ItemForm, ProdutoAddForm, ProdutoCategoriaForm
import logging
from produtos.models import Categoria, Produto
from django.views.generic.base import TemplateView

my_log = logging.getLogger('django')


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desconto()
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['n_ped'] = Venda.objects.num_pedidos()
        data['n_ped_nfe'] = Venda.objects.num_ped_nefe()

        return render(request, 'vendas/dashboard.html', data)

class PagamentoView(LoginRequiredMixin, TemplateView):
    template_name = "vendas/pagamento.html"

    def get_context_data(self, **kwargs):
        context = super(PagamentoView, self).get_context_data(**kwargs)

        return context

class PagamentoView2(LoginRequiredMixin, TemplateView):
    template_name = "vendas/pagamento2.html"

    def get_context_data(self, **kwargs):
        context = super(PagamentoView2, self).get_context_data(**kwargs)
        print(self.kwargs.get('venda'))

        venda = Venda.objects.get(id=self.kwargs.get('venda'))


        total_venda = venda.itemsvenda_set.all().aggregate(
            total_venda =Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['total_venda'] or 0
        total_venda = total_venda - float(venda.impostos) - float(venda.desconto)

        # context = ClienteForm(instance=cliente OR None)
        context['form_item'] = ItemPedidoForm()

        context['desconto'] = float(venda.desconto)
        context['venda'] = venda
        print(venda.id)
        context['itens'] = venda.itemsvenda_set.all().annotate(
            total_item=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )
        context['subtotal'] = venda.itemsvenda_set.all().aggregate(
            subtotal=Sum((F('quantidade') * F('produto__preco')) , output_field=FloatField())
        )['subtotal'] or 0

        context['total_desconto'] = (venda.itemsvenda_set.all().aggregate(
            total_desconto=Sum(( F('desconto')), output_field=FloatField())
        )['total_desconto'] or 0) + float(venda.desconto)

        context['total_venda'] = total_venda

        return context



class NovoPedido(View):

    def get(self, request):

        data = {}
        data_get = {}

        data_get['clientes'] = VendaForm(request.POST, request.FILES)
        data_get['form_produto'] = ProdutoAddForm()
        data_get['ProdutoCategoriaForm'] = ProdutoCategoriaForm()
        # data_get['clientes'] = VendaForm(instance=venda)
        return render(request, 'vendas/novo-pedido.html', data_get)

    def post(self, request):
        data = {}

        vendaform = VendaForm(request.POST or None)

        data['cliente'] = request.POST['cliente']
        data['venda_id'] = request.POST['venda_id']

        if data['venda_id']:
            print("tem id aqui")
            venda = Venda.objects.get(id=data['venda_id'])
            vendaform = VendaForm(request.POST or None, instance=venda)

            if vendaform.is_valid():
                venda = vendaform.save(commit=False)
                print(venda.save())
                vendaform.clean()
                return redirect('edit-pedido', venda=venda.pk)

        else:
            if vendaform.is_valid():
                print(vendaform.cleaned_data.get('cliente_id'))
                venda = vendaform.save(commit=False)
                venda.vendedor = request.user
                venda.save()
                print('venda ', venda.pk, ' criada com sucesso!')

                return redirect('edit-pedido', venda=venda.pk)


def add_item_ajax(request):
    venda_id = request.POST['venda_id']
    id_produto = request.POST['id_produto']
    desconto_produto = request.POST['desconto_produto']
    quantidade_produto = request.POST['quantidade_produto']
    print('venda: ', venda_id)
    print('id_produto: ', id_produto)
    print('desconto_produto: ', desconto_produto)
    print('quantidade_produto: ', quantidade_produto)

    item = ItemsVenda.objects.filter(produto_id=id_produto, venda_id=venda_id)
    print(item)

    if item:

        data = ''
        print(item)
        item_add = Produto.objects.get(id=id_produto)

        response_data = {}
        response_data['itens'] = {"descricao": item_add.descricao}
        response_data['result'] = "error"
        response_data['mensagem'] = 'Item já incluso no pedido, por favor edite!'

        print([response_data])
        print(json.dumps([response_data]))
        # qs_json = serializers.serialize('json', ItemsVenda.objects.filter(venda_id=venda_id))
        return HttpResponse(json.dumps([response_data]), content_type='application/json')
    else:
        a = ItemsVenda.objects.filter(venda_id=venda_id)

        produto_estoque = Estoque.objects.get(produto_id=id_produto)
        produto_estoque.alterar_estoque(id_produto, int(quantidade_produto))

        item = ItemsVenda.objects.create(
            produto_id=id_produto, quantidade=quantidade_produto,
            desconto=desconto_produto, venda_id=venda_id)

        venda = Venda.objects.get(id=venda_id)

        qs_json = (serializers.serialize('json', ItemsVenda.objects.filter(venda_id=venda_id)))
        print(qs_json)

        response_data = {}
        list_produtos = []
        for produto_venda in ItemsVenda.objects.filter(venda_id=venda_id):
            response = {'id_venda': produto_venda.venda.pk,
                        'id_item_pedido': produto_venda.pk,
                        'produto_id': str(produto_venda.produto.pk),
                        'produto_name': str(produto_venda.produto.descricao),
                        'produto_preco': str(produto_venda.produto.preco),
                        'quantidade': str(produto_venda.quantidade),
                        'desconto': str(produto_venda.desconto)}
            list_produtos.append(response)


        response_data['itens'] = list_produtos
        response_data['result'] = 'error'
        response_data['mensagem'] = 'Item adicionado com sucesso'
        print(list_produtos)
        # print(json.dumps([response_data]))

        return HttpResponse(json.dumps([response_data]), content_type='application/json')


class NovoItemPedido(View):
    def get(self, request, pk):
        data = {}
        data_get = {}

        data_get['clientes'] = VendaForm(request.POST, request.FILES)
        data_get['form_produto'] = ProdutoAddForm()
        data_get['ProdutoCategoriaForm'] = ProdutoCategoriaForm()
        # data_get['clientes'] = VendaForm(instance=venda)
        return render(request, 'vendas/novo-pedido.html', data_get)

    def post(self, request, venda):
        data = {}
        item = ItemsVenda.objects.filter(produto_id=request.POST['produto_list'], venda_id=venda)

        produtoform = ProdutoAddForm(request.POST)

        # verificar item
        if item:
            print(request.POST['produto_list'])
            data['mensagem'] = 'Item já incluso no pedido, por favor edite!'
            item = item[0]
        else:
            print(item)
            print(request.POST['produto_list'])
            data['mensagem'] = ''
            produto_qted = -int(request.POST['quantidade'])

            id_produto = int(request.POST['produto_list'])

            produto_estoque = Estoque.objects.get(produto_id=id_produto)

            produto_estoque.alterar_estoque(id_produto, produto_qted)
            # Produto.objects.filter(id=request.POST['produto_id']).update(field=F('qted') + request.POST['quantidade'])
            item = ItemsVenda.objects.create(
                produto_id=request.POST['produto_list'], quantidade=request.POST['quantidade'],
                desconto=request.POST['desconto'], venda_id=venda)

        venda = Venda.objects.get(id=venda)
        data['clientes'] = VendaForm(instance=venda)
        data['item'] = item
        data['form_item'] = ItemPedidoForm()
        data['form_produto'] = ProdutoAddForm()
        data['ProdutoCategoriaForm'] = ProdutoCategoriaForm()

        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda
        data['itens'] = item.venda.itemsvenda_set.all()

        return render(
            request, 'vendas/novo-pedido.html', data)


class ListaVendas(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'lista-vendas'

    def get(self, request):
        my_log.debug('Acessaram a listagem de vendas: ')

        vendas = Venda.objects.all()
        count_vendas = vendas.count()
        # count 4
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas, 'count_vendas': count_vendas})


class EditPedido(View):
    def get(self, request, venda):
        data = {}
        STATUS = VendaStatus

        venda = Venda.objects.get(id=venda)
        vendaform = VendaForm(instance=venda or None)

        data['clientes'] = vendaform
        data['form_produto'] = ProdutoAddForm()
        data['ProdutoCategoriaForm'] = ProdutoCategoriaForm()
        # form = ClienteForm(instance=cliente OR None)
        data['form_item'] = ItemPedidoForm()

        data['desconto'] = float(venda.desconto)
        data['venda'] = venda
        print(venda.id)
        data['itens'] = venda.itemsvenda_set.all()
        # print(venda.status.VendaStatus)

        return render(
            request, 'vendas/novo-pedido.html', data)


class DeletePedido(View):
    def get(self, request, venda):
        venda = Venda.objects.get(id=venda)
        return render(
            request, 'vendas/delete-pedido-confirm.html', {'venda': venda})

    def post(self, request, venda):
        venda = Venda.objects.get(id=venda)

        itens_venda = venda.itemsvenda_set.all()
        for item in itens_venda:
            # item_pedido = ItemsVenda.objects.get(id=item)

            produto_pedido = Produto.objects.get(id=item.produto.pk)
            produto_estoque = Estoque.objects.get(produto=item.produto.pk)
            Qted_estoque = int(item.quantidade)

            print(produto_estoque.produto.pk)
            produto_estoque.alterar_estoque(item.produto.pk, Qted_estoque)

        venda.delete()
        return redirect('lista-vendas')


class DeleteItemPedido(View):
    def get(self, request, item):
        item_pedido = ItemsVenda.objects.get(id=item)
        return render(
            request, 'vendas/delete-itempedido-confirm.html', {'item_pedido': item_pedido})

    def post(self, request, item):
        print(item)
        # id_produto = int(request.POST['produto_id'])
        produto = Produto.objects.filter(id=item)
        item_pedido = ItemsVenda.objects.get(id=item)

        produto_qted = item_pedido.quantidade
        produto_estoque = Estoque.objects.get(produto=item_pedido.produto)

        produto_estoque.alterar_estoque(item_pedido.produto, produto_qted)
        venda_id = item_pedido.venda.id
        item_pedido.delete()

        return redirect('edit-pedido', venda=venda_id)


class EditItemPedido(View):
    def get(self, request, item):
        data_get = {}
        print(item)
        item_pedido = ItemsVenda.objects.get(id=item)
        val_item = item_pedido.produto.preco
        form = ItemForm(instance=item_pedido)

        data_get['form_produto'] = ProdutoAddForm()
        data_get['ProdutoCategoriaForm'] = ProdutoCategoriaForm()
        data_get['item_pedido']: item_pedido
        data_get['form'] = form
        data_get['val_item'] = val_item
        return render(
            request,
            'vendas/edit-itempedido.html',
            data_get)

    def post(self, request, item):
        # print(item)

        item_pedido = ItemsVenda.objects.get(id=item)
        produto_pedido = Produto.objects.get(id=item_pedido.produto.pk)
        produto_estoque = Estoque.objects.get(produto=item_pedido.produto.pk)
        Qted_estoque = int(item_pedido.quantidade) - int(request.POST['quantidade'])

        print(produto_estoque.produto.pk)
        produto_estoque.alterar_estoque(item_pedido.produto.pk, Qted_estoque)
        # print(produto_pedido)
        # print(item_pedido.produto.pk)
        # print(item_pedido.produto.qted)

        # produto_pedido.qted += Qted_estoque
        # produto_pedido.save()
        # print('antes estoque alterado--------------------------')
        # self.produto.save()

        # print('antes----', int(item_pedido.quantidade) - int(request.POST['quantidade']))
        item_pedido.quantidade = request.POST['quantidade']
        item_pedido.desconto = request.POST['desconto']

        item_pedido.save()
        venda_id = item_pedido.venda.id

        return redirect('edit-pedido', venda=venda_id)


def filtra_produtos(request):
    id_categoria = request.POST.get['outro_param']
    print( request.POST.get['outro_param'] ,'ddd')

    categoria = Categoria.objects.get(id=id_categoria)

    qs_json = serializers.serialize('json', categoria.produto_set.all())
    return HttpResponse(qs_json, content_type='application/json')
