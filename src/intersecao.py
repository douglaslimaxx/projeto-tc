# coding: utf-8
import sys
from classes import *
from leitor import *

def intersecao(automato1, automato2):
    novo_estado_inicial = automato1.estado_inicial + automato2.estado_inicial
    estados = []
    transicoes = []
    estados_aceitacao = []
    for au1 in automato1.transicoes:
        
        for au2 in automato2.transicoes:

            if ((au1.destino in automato1.estados_aceitacao) and (au2.destino in automato2.estados_aceitacao)):
                if ((au1.destino + au2.destino) not in estados_aceitacao):
                    estados_aceitacao.append(au1.destino + au2.destino)

            if (au1.entrada == au2.entrada):
                transicoes.append(Transicao(au1.origem + au2.origem, au1.entrada, au1.destino + au2.destino))

            if ((au1.destino + au2.destino) not in estados):
                    estados.append(au1.destino + au2.destino)    
           
    return Automato(estados, novo_estado_inicial, estados_aceitacao, transicoes)

print("\nVocê Escolheu a Interseção")
args = sys.argv[1:]
caminho1, caminho2 = args[0:2]
automato = intersecao(importa_automato(caminho1), importa_automato(caminho2))

print("\n----AUTOMATO RESULTANTE----")
imprimir_automato(automato)