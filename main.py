# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada
#
# # fila_teste = FilaNormal()
# # fila_teste.atualiza_fila()
# # fila_teste.atualiza_fila()
# # fila_teste.atualiza_fila()
# # print(fila_teste.chama_cliente(10))
#
# fila_teste_2 = FilaNormal()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# print(fila_teste_2.chama_cliente(10))
# # print(fila_teste_2.estatisticas('20/10/1999', 197, 'detail'))

teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.estatisticas(EstatisticaDetalhada('20/10/1999', 197)))
