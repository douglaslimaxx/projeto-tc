from classes import *

def concatenacao(automato1,automato2):

    aceitacao = automato2.estados_aceitacao
    estados = automato1.estados + automato2.estados
    transicoes = automato1.transicoes + automato2.transicoes

    for estado_final in automato1.estados_aceitacao:
        transicoes.append(Transicao(estado_final, "e", automato2.estado_inicial))

    return Automato(estados, automato1.estado_inicial, aceitacao, transicoes)

automato1 = Automato(["a","b","z"],"a",["b","z"],[Transicao("a","0","b"),Transicao("a","1","a"),Transicao("a","1","z")])
automato2 = Automato(["c","d"],"c",["d"],[Transicao("c","0","d"),Transicao("c","1","c")])

automato_resultante = concatenacao(automato1,automato2)

print(automato_resultante.estado_inicial)
print(automato_resultante.estados_aceitacao)
print(automato_resultante.estados)
for transicao in automato_resultante.transicoes:
    print(transicao)
