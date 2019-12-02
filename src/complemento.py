# coding: utf-8
import sys
from classes import *
from leitor import *

def complemento(automato):

    estados_aceitacao = [
        estado for estado in automato.estados if estado not in automato.estados_aceitacao
    ]

    return Automato(automato.estados, automato.estado_inicial, estados_aceitacao, automato.transicoes)

print("\nVocê Escolheu o Complemento")
args = sys.argv[1:]
caminho1 = args[0]
automato = complemento(importa_automato(caminho1))

print("\n----AUTOMATO RESULTANTE----")
imprimir_automato(automato)