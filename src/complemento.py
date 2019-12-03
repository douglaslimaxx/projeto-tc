# coding: utf-8
import sys
from classes import *
from leitor import *
from operacoes import *

print("\nVocê Escolheu o Complemento")
args = sys.argv[1:]
caminho1 = args[0]
automato = complemento(importa_automato(caminho1))

print("\n----AUTOMATO RESULTANTE----")
imprimir_automato(automato)