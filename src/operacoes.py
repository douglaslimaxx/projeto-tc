# coding: utf-8
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

def complemento(automato):

    estados_aceitacao = [
        estado for estado in automato.estados if estado not in automato.estados_aceitacao
    ]

    return Automato(automato.estados, automato.estado_inicial, estados_aceitacao, automato.transicoes)


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

# def concatenacao(automato1, automato2):

#     aceitacao = automato2.estados_aceitacao
#     estados = automato1.estados + automato2.estados
#     transicoes = automato1.transicoes + automato2.transicoes

#     for estado_final in automato1.estados_aceitacao:
#         transicoes.append(
#             Transicao(estado_final, "e", automato2.estado_inicial))

#     return Automato(estados, automato1.estado_inicial, aceitacao, transicoes)