# coding: utf-8
import sys
from leitor import importa_automato

args = sys.argv[1:]
caminho, entrada = args[0:2]
automato = importa_automato(caminho)

print "Estados:", automato.estados
print "Estado inicial:", automato.estado_inicial
print "Estados de aceitação:", automato.estados_aceitacao
print "Transições:"
for transicao in automato.transicoes:
  print transicao