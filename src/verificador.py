# coding: utf-8
import sys
from leitor import importa_automato

def verifica(automato, palavra):
    estado_atual = [automato.estado_inicial]
    print("Estado        Palavra")
    for i in range(len(palavra)):
        print("%s             %s" % (estado_atual, palavra[i:len(palavra)]))
        estado_atual = efetua_transicao(palavra[i], automato, estado_atual)
    print("%s             %s" % (estado_atual, "e"))
    for k in estado_atual:
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
    if(resultado):
        print("A palava %s foi aceita" % palavra)
    else:
        print("A palava %s não foi aceita" % palavra)

args = sys.argv[1:]
caminho, entrada = args[0:2]
automato = importa_automato(caminho)

print("\n----VERIFICAÇÃO----")
verificador(automato, entrada)