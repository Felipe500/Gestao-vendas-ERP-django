from model_utils import Choices


ESPECIE = '0'
CARTAO = '1'
PIX = '2'
DEPOSITO = '3'

SAIDA = '0'
ENTRADA = '1'

STATUS_VENDA = Choices(
    (SAIDA, 'saida'),
    (ENTRADA, 'entrada')
)
FORMA_PG = Choices(
    (ESPECIE, 'ESPECIE'),
    (CARTAO, 'CARTAO'),
    (PIX, 'PIX'),
    (DEPOSITO, 'DEPOSITO'),
)

