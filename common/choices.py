from model_utils import Choices

STATUS_CONTENT = Choices(
    ('0', 'saida'),
    ('1', 'entrada')
)

STATUS_Venda = Choices(
    ('0', 'saida'),
    ('1', 'entrada')
)

ABERTA = 'AB', 'Aberta'
FECHADA = 'FE', 'Fechada'
PROCESSANDO = 'PR', 'Processando'
DESCONHECIDO = 'DC', 'Desconhecido'