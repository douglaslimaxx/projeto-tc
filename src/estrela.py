# coding: utf-8
import sys
from classes import *
from leitor import *


def estrela(automato):

    novo_estado_inicial = "NOVO"
    transicoes = automato.transicoes
    transicoes.append(Transicao(novo_estado_inicial,
                                "e", automato.estado_inicial))

    estados = automato.estados
    estados.append(novo_estado_inicial)

    for estado_final in automato.estados_aceitacao:
        transicoes.append(
            Transicao(estado_final, "e", automato.estado_inicial))

    estados_aceitacao = automato.estados_aceitacao
    estados_aceitacao.append(novo_estado_inicial)

    return Automato(estados, novo_estado_inicial, estados_aceitacao, transicoes)

print("\nVocê Escolheu o Complemento")
args = sys.argv[1:]
caminho1 = args[0]
automato = estrela(importa_automato(caminho1))

print("\n----AUTOMATO RESULTANTE----")
imprimir_automato(automato)