import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View

from produtos.models import Produto, Estoque
from .models import Venda, ItemsVenda,  VendaStatus
from django.db.models import  Sum, F, FloatField,Min, Max, Avg
from .forms import VendaForm, ItemPedidoForm,ItemForm
import logging


my_log = logging.getLogger('django')


class DashboardView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):

            return HttpResponse('Acesso negado, voce precisa de permissao!')

        return super(DashboardView, self).dispatch(request, *args, **kwargs)
    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desconto()
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['n_ped'] = Venda.objects.num_pedidos()
        data['n_ped_nfe'] = Venda.objects.num_ped_nefe()

        return render( request,'vendas/dashboard.html', data)

class NovoPedido(View):

    def get(self, request):

        data={}
        data_get = {}

        data_get['clientes'] = VendaForm(request.POST, request.FILES)

        #data_get['clientes'] = VendaForm(instance=venda)
        return render(request, 'vendas/novo-pedido.html',data_get)

    def post(self, request):

        data = {}

        data['form_item'] = ItemPedidoForm()
        vendaform = VendaForm(request.POST or None)

        data['cliente']= request.POST['cliente']
        data['venda_id'] = request.POST['venda_id']
        data['clientes'] = vendaform


        if data['venda_id']:
            print("tem id aqui")
            venda = Venda.objects.get(id=data['venda_id'])
            vendaform = VendaForm(request.POST or None, instance=venda)

            if vendaform.is_valid():
                form = vendaform.save(commit=False)
                print(form.save())

            itens = venda.itemsvenda_set.all()
            data['venda'] = venda
            data['itens'] = itens





        else:
            print("não tem id aqui")

            if vendaform.is_valid():

                print(vendaform.cleaned_data.get('cliente_id'))
                form = vendaform.save()
                print('venda ',form.pk,' criada com sucesso!')
                venda = Venda.objects.get(id=form.pk)
                itens = venda.itemsvenda_set.all()
                data['venda'] = venda
                data['itens'] = itens

        return render(
            request, 'vendas/novo-pedido.html', data)

class NovoItemPedido(View):
    def get(self, request, pk):
        data = {}
        data_get = {}

        data_get['clientes'] = VendaForm(request.POST, request.FILES)

        # data_get['clientes'] = VendaForm(instance=venda)
        return render(request, 'vendas/novo-pedido.html', data_get)

    def post(self, request, venda):
        data = {}
        item = ItemsVenda.objects.filter(produto_id=request.POST['produto_id'], venda_id=venda)

        if item:
            data['mensagem'] = 'Item já incluso no pedido, por favor edite!'
            item = item[0]
        else:
            print(item)
            data['mensagem'] = ''
            produto_qted = -int(request.POST['quantidade'])

            id_produto = int(request.POST['produto_id'])

            produto_estoque = Estoque.objects.get(produto_id=id_produto)

            produto_estoque.alterar_estoque(id_produto, produto_qted)

            #Produto.objects.filter(id=request.POST['produto_id']).update(field=F('qted') + request.POST['quantidade'])
            item = ItemsVenda.objects.create(
            produto_id=request.POST['produto_id'], quantidade=request.POST['quantidade'],
            desconto=request.POST['desconto'], venda_id=venda)

        venda = Venda.objects.get(id=venda)
        data['clientes'] = VendaForm( instance=venda)
        data['item'] = item
        data['form_item'] = ItemPedidoForm()

        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda
        data['itens'] = item.venda.itemsvenda_set.all()

        return render(
            request, 'vendas/novo-pedido.html', data)

class ListaVendas( LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'lista-vendas'



    def get(self, request):

        my_log.debug('Acessaram a listagem de vendas: ')


        vendas = Venda.objects.all()
        count_vendas = vendas.count()
        #count 4
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas, 'count_vendas':count_vendas})

class EditPedido(View):
    def get(self, request, venda):
        data = {}
        STATUS = VendaStatus

        venda = Venda.objects.get(id=venda)
        vendaform = VendaForm(instance=venda or None)
        data['clientes'] = vendaform
        #form = ClienteForm(instance=cliente OR None)
        data['form_item'] = ItemPedidoForm()

        data['desconto'] = float(venda.desconto)
        data['venda'] = venda
        print(venda.id)
        data['itens'] = venda.itemsvenda_set.all()
        #print(venda.status.VendaStatus)

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
            #item_pedido = ItemsVenda.objects.get(id=item)

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
        #id_produto = int(request.POST['produto_id'])
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
        print(item)
        item_pedido = ItemsVenda.objects.get(id=item)
        val_item = item_pedido.produto.preco
        form = ItemForm(instance=item_pedido)

        return render(
            request,
            'vendas/edit-itempedido.html',
            {'item_pedido': item_pedido,
            'form':form,
            'val_item':val_item,})

    def post(self, request, item):

        #print(item)

        item_pedido = ItemsVenda.objects.get(id=item)
        produto_pedido = Produto.objects.get(id=item_pedido.produto.pk)
        produto_estoque = Estoque.objects.get(produto=item_pedido.produto.pk)
        Qted_estoque = int(item_pedido.quantidade) - int(request.POST['quantidade'])

        print(produto_estoque.produto.pk)
        produto_estoque.alterar_estoque(item_pedido.produto.pk,Qted_estoque)
        #print(produto_pedido)
        #print(item_pedido.produto.pk)
        #print(item_pedido.produto.qted)


        #produto_pedido.qted += Qted_estoque
        #produto_pedido.save()
        #print('antes estoque alterado--------------------------')
        #self.produto.save()

        #print('antes----', int(item_pedido.quantidade) - int(request.POST['quantidade']))
        item_pedido.quantidade = request.POST['quantidade']
        item_pedido.desconto = request.POST['desconto']

        item_pedido.save()
        venda_id = item_pedido.venda.id

        return redirect('edit-pedido', venda=venda_id)