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
