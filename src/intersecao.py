# coding: utf-8
import sys
from classes import *
from leitor import *
from operacoes import *

print("\nVocê Escolheu a Interseção")
args = sys.argv[1:]
caminho1, caminho2 = args[0:2]
automato = intersecao(importa_automato(caminho1), importa_automato(caminho2))

print("\n----AUTOMATO RESULTANTE----")
imprimir_automato(automato)