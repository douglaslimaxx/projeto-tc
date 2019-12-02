# coding: utf-8
import sys
from classes import *
from leitor import *

def uniao(automato1, automato2):
    novo_estado_inicial = "NOVO"

    transicoes = automato1.transicoes + automato2.transicoes
    transicoes.append(Transicao(novo_estado_inicial,
                                "e", automato1.estado_inicial))
    transicoes.append(Transicao(novo_estado_inicial,
                                "e", automato2.estado_inicial))

    estados = automato1.estados + automato2.estados
    estados.append(novo_estado_inicial)

    estados_aceitacao = automato1.estados_aceitacao + automato2.estados_aceitacao

    return Automato(estados, novo_estado_inicial, estados_aceitacao, transicoes)

print("\nVocê Escolheu a União")
args = sys.argv[1:]
caminho1, caminho2 = args[0:2]
automato = uniao(importa_automato(caminho1), importa_automato(caminho2))

print("\n----AUTOMATO RESULTANTE----")
imprimir_automato(automato)