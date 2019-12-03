# coding: utf-8
import sys
from classes import *
from leitor import *

args = sys.argv[1:]
caminho = args[0]
automato = importa_automato(caminho)
afn = AutomatoNaoDeterministico(
    automato.estados, automato.estado_inicial, automato.estados_aceitacao, automato.transicoes)

imprimir_automato(afn)
afd = AutomatoDeterministico()
afd.converter_a_partir_de_afn(afn)

imprimir_automato(afd)
