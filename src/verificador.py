from leitor import *
from classes import *

def verificador(automato, palavra):
    estado_atual = automato.estado_inicial()
    for i in palavra:
        estado_atual = efetuatransicao(i, automato, estado_atual)
    if(estado_atual in automato.estados_aceitacao()):
        return True
    else:
        return False

def efetuatransicao(terminal, automato, estado_atual):
    for i in automato.transicoes():
        if((estado_atual == i.origem()) and (terminal == i.entrada())):
            return i.destino()