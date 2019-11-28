# coding: utf-8


class Automato:
    """
    Representação de um autômato.

    Armazena os estados, estado inicial, estado de aceitação e uma lista de transições
    que são objetos do tipo Transicao.
    """

    def __init__(self, estados, estado_inicial, estados_aceitacao, transicoes):
        self._estados = estados
        self._estado_inicial = estado_inicial
        self._estados_aceitacao = estados_aceitacao
        self._transicoes = transicoes

    @property
    def estados(self):
        return self._estados

    @property
    def estado_inicial(self):
        return self._estado_inicial

    @property
    def estados_aceitacao(self):
        return self._estados_aceitacao

    @property
    def transicoes(self):
        return self._transicoes

    def get_transicoes_dict(self):
        transicoes_dict = {}

        for transicao in self._transicoes:
            origem = transicao.origem
            destino = transicao.destino
            entrada = transicao.entrada

            key = (origem, entrada)

            if key in transicoes_dict:
                transicoes_dict[key].append(destino)
            else:
                transicoes_dict[key] = [destino]

        return transicoes_dict


class Transicao:
    """
    Representação de uma transição de um autômato. 
    Armazena o estado de origem, a entrada e o estado de destino.

    Origem é o estado em que o automato se encontra, entrada é um símbolo do alfabeto
    que leva a um estado de Destino.
    """

    def __init__(self, origem, entrada, destino):
        self._origem = origem
        self._entrada = entrada
        self._destino = destino

    @property
    def origem(self):
        return self._origem

    @property
    def entrada(self):
        return self._entrada

    @property
    def destino(self):
        return self._destino

    def __str__(self):
        """
        Representação textual de uma transição na forma "(estado_origem, entrada) => (estado_destino)"
        """
        return "(%s, %s) => %s" % (self._origem, self._entrada, self._destino)

    def __eq__(self, other):
        if isinstance(other, Transicao):
            return (
                self._origem == other._origem and
                self._entrada == other._entrada and
                self._destino == other._destino
            )
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class AutomatoNaoDeterministico(Automato):

    def __init__(self, estados=None, estado_inicial=None, estados_aceitacao=None, transicoes=None):
        self._estados = estados if estados is not None else []
        self._estado_inicial = estado_inicial if estado_inicial is not None else 0
        self._estados_aceitacao = estados_aceitacao if estados_aceitacao is not None else []
        self._transicoes = transicoes if transicoes is not None else []


class AutomatoDeterministico(Automato):

    def __init__(self, estados=None, estado_inicial=None, estados_aceitacao=None, transicoes=None):
        self._estados = estados if estados is not None else []
        self._estado_inicial = estado_inicial if estado_inicial is not None else 0
        self._estados_aceitacao = estados_aceitacao if estados_aceitacao is not None else []
        self._transicoes = transicoes if transicoes is not None else []

    def converter_a_partir_de_afn(self, afn):
        self._estados = []
        self._transicoes = []
        self._estado_inicial = afn.estado_inicial
        self._estados_aceitacao = afn.estados_aceitacao
        self._estados.append(afn.estado_inicial)

        afn_transicoes_dict = afn.get_transicoes_dict()

        for estado_afd in self._estados:
            for simbolo in [0, 1]:
                key = (estado_afd, simbolo)

                if key in afn_transicoes_dict:
                    destino = afn_transicoes_dict[key]
                    destino = destino[0] if len(
                        destino) == 1 else tuple(destino)

                    if destino not in self._estados:
                        self._estados.append(destino)

                    transicao = Transicao(estado_afd, simbolo, destino)
                    if transicao not in self._transicoes:
                        self._transicoes.append(transicao)
                else:
                    transicao = Transicao(estado_afd, simbolo, estado_afd)
                    if transicao not in self._transicoes:
                        self._transicoes.append(transicao)
