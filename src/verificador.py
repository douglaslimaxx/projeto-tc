# coding: utf-8
from leitor import *
from classes import *

def verifica(automato, palavra):
    estados_atuais = automato.estado_inicial
    for i in palavra:
        estados_atuais = efetua_transicao(i, automato, estados_atuais)
        print(estados_atuais)
    for k in estados_atuais:
        if (k in automato.estados_aceitacao):
            return True
    return False

def efetua_transicao(terminal, automato, estado_atual):
    destinos = []
    for i in automato.transicoes:
        for j in estado_atual:
            if((j == i.origem) and ((terminal == i.entrada) or i.entrada == "e")):
                destinos.append(i.destino)
    return destinos

def verificador(automato, palavra):
    resultado = verifica(automato, palavra)
    print(resultado)
    if(resultado):
        print("A palavra %s foi aceita" % palavra)
    else:
        print("A palavra %s não foi aceita" % palavra)