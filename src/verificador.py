# coding: utf-8
import sys
from leitor import importa_automato

def verifica(automato, palavra):
    estado_atual = automato.estado_inicial
    print("Estado        Palavra")
    for i in range(len(palavra)):
        print("%s             %s" % (estado_atual, palavra[i:len(palavra)]))
        estado_atual = efetua_transicao(palavra[i], automato, estado_atual)
    print("%s             %s" % (estado_atual, "e"))
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

args = sys.argv[1:]
caminho, entrada = args[0:2]
automato = importa_automato(caminho)

print("\n----VERIFICAÇÃO----")
verificador(automato, entrada)