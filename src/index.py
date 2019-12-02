# coding: utf-8
import sys
from leitor import importa_automato
from verificador import verificador

args = sys.argv[1:]
caminho, entrada = args[0:2]
automato = importa_automato(caminho)

print("\n----VERIFICAÇÃO----")
verificador(automato, entrada)
