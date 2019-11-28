from classes import *


def uniao(automato1, automato2):
    novo_estado_inicial = "novo"

    transicoes = automato1.transicoes + automato2.transicoes
    transicoes.append(Transicao(novo_estado_inicial,
                                "e", automato1.estado_inicial))
    transicoes.append(Transicao(novo_estado_inicial,
                                "e", automato2.estado_inicial))

    estados = automato1.estados + automato2.estados
    estados.append(novo_estado_inicial)

    estados_aceitacao = automato1.estados_aceitacao + automato2.estados_aceitacao

    return Automato(estados, novo_estado_inicial, estados_aceitacao, transicoes)


def complemento(automato):

    estados_aceitacao = [
        estado for estado in automato.estados if estado not in automato.estados_aceitacao
    ]

    return Automato(automato.estados, automato.estado_inicial, estados_aceitacao, automato.transicoes)


def estrela(automato):

    novo_estado_inicial = "novo"
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


automato1 = Automato(["a", "b", "z"], "a", ["b", "z"], [Transicao(
    "a", "0", "b"), Transicao("a", "1", "a"), Transicao("a", "1", "z")])
automato2 = Automato(["c", "d", "e", "f"], "c", ["d"], [
                     Transicao("c", "0", "d"), Transicao("c", "1", "c"), Transicao("d", "1", "e"), Transicao("d", "0", "f")])

automato_resultante = estrela(automato2)

print(automato_resultante.estado_inicial)
print(automato_resultante.estados_aceitacao)
print(automato_resultante.estados)
for transicao in automato_resultante.transicoes:
    print(transicao)
