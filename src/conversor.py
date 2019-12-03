# coding: utf-8
import sys
from classes import *
from leitor import *

args = sys.argv[1:]
caminho = args[0]
automato = importa_automato(caminho)
afn = AutomatoNaoDeterministico(automato.estados, automato.estado_inicial, automato.estados_aceitacao, automato.transicoes)

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
