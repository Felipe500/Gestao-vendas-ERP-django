from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto, Estoque
from .forms import ProdutoForm,EstoqueForm



@login_required
def produtos_list(request):
    produtos = Produto.objects.using('default').all()
    return render(request, 'produtos/produtos_list.html', {'produtos': produtos})


def Produto_update(request, id):
    produto_id = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto_id)

    if form.is_valid():
        form = form.save(commit=False)
        form.save(using='default')
        return redirect('produto_list')

    return render(request, 'produtos/produto_update.html', {'form': form})

@login_required
def Produto_Novo(request):

    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.save(using='default')
        return redirect('produto_list')

    return render(request, 'produtos/produto_novo.html', {'form': form})

@login_required
def Produto_Delete(request, id):
    prod = Produto.objects.using('default').get(id=id)

    if request.method == 'POST':
        prod.delete(using='default')
        return redirect('produto_list')

    return render(request, 'produtos/produto_delete.html', {'produto': prod})

@login_required
def Estoque_produtos(request):
    estoque = Estoque.objects.using('default').all()
    return render(request, 'produtos/estoque_produtos.html', {'produto_estoque': estoque})

@login_required
def Editar_Estoque(request, id):
    estoque_id = get_object_or_404(Estoque, pk=id)
    form = EstoqueForm(request.POST or None, instance=estoque_id)

    if form.is_valid():
        form = form.save(commit=False)
        form.save(using='default')
        return redirect('estoque_produtos')

    return render(request, 'produtos/estoque_form.html', {'form': form})