# coding: utf-8
import sys
from leitor import importa_automato
from verificador import verificador

args = sys.argv[1:]
caminho, entrada = args[0:2]
automato = importa_automato(caminho)

print("\n----AUTOMATO----")
print("Estados: %s" % automato.estados)
print("Estado inicial: %s" % automato.estado_inicial)
print("Estados de aceitação: %s" % automato.estados_aceitacao)
print("Transições:")
for transicao in automato.transicoes:
    print(transicao)
print("\n----VERIFICAÇÃO----")
verificador(automato, entrada)
