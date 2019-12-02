from classes import *

afn = AutomatoNaoDeterministico(
    ['A', 'B', 'C'], 'A', ['C'], [Transicao('A', 0, 'A'), 
    Transicao('A', 1, 'A'), Transicao('A', 0, 'B'),
    Transicao('B', 0, 'C'), Transicao('B', 1, 'C'),
    Transicao('C', 0, 'C'), Transicao('C', 1, 'C')])

print("NÃO DETERMINÍSTICO: ")
print("Estados:", afn.estados)
print("Estado inicial:", afn.estado_inicial)
print("Estados de aceitação:", afn.estados_aceitacao)
print("Transições:")
for transicao in afn.transicoes:
    print(transicao)

afd = AutomatoDeterministico()

afd.converter_a_partir_de_afn(afn)

print("DETERMINÍSTICO")
print("Estados:", afd.estados)
print("Estado inicial:", afd.estado_inicial)
print("Estados de aceitação:", afd.estados_aceitacao)
print("Transições:")
for transicao in afd.transicoes:
    print(transicao)
