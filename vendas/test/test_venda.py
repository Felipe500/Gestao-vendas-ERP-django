
from django.test import TestCase
from vendas.models import Venda, ItemsVenda
from produtos.models import Produto

class VendaTestCase(TestCase):
    def setUp(self):
        """CONFIGURAÇÃO DE TESTES"""
        self.venda = Venda.objects.create(numero='12311', desconto=10)
        self.produto = Produto.objects.create(
            descricao = 'produto 1', preco=10
        )

    def test_verifica_num_vendas(self):
        """TESTE DE NUMERO DE VENDAS"""
        #num = Venda.objects.filter(numero='12311').count
        assert Venda.objects.all().count() == 1

    def test_valor_venda(self):
        """VERIFICAR O VALOR TOTAL DA VENDA"""
        ItemsVenda.objects.create(venda=self.venda, produto=self.produto, quantidade=10, desconto=10)
        assert self.venda.valor == 80
    def test_inclusao_lista_itens(self):
        """VERIFICAR SE ITENS ESTÃO SENDO INCLUSOS"""
        item = ItemsVenda.objects.create(
        venda=self.venda, produto=self.produto, quantidade=1, desconto=0)
        self.assertIn(item, self.venda.itemsvenda_set.all())

    def test_status_nfe(self):
        """VERIFICAR STATUS NFE: PADRAO FALSE"""
        self.assertFalse(self.venda.nfe_emitida)
    def test_status_venda(self):
        """FORÇAR POSSIVEL ALTERAÇÃO DE STATUS DA VENDA"""
        self.venda.status = 'PC'
        self.venda.save()
        self.assertEqual(self.venda.status, 'PC')





