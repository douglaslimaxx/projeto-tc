# coding: utf-8
from leitor import *
from classes import *

def verifica(automato, palavra):
    estado_atual = automato.estado_inicial
    for i in palavra:
        estado_atual = efetua_transicao(i, automato, estado_atual)
    if(estado_atual in automato.estados_aceitacao):
        return True
    else:
        return False

def efetua_transicao(terminal, automato, estado_atual):
    for i in automato.transicoes:
        if((estado_atual == i.origem) and (terminal == i.entrada)):
            return i.destino

def verificador(automato, palavra):
    resultado = verifica(automato, palavra)
    if(resultado):
        print("A palava %s foi aceita" % palavra)
    else:
        print("A palava %s não foi aceita" % palavra)