# coding: utf-8
from classes import *

def converte_transicao(raw):
  origem, destino, entrada = raw.split(' ')
  return Transicao(origem, entrada, destino)

def importa_automato(caminho):
  """ Importa um automato presente em um arquivo

  Args: 
    caminho (str): caminho para o arquivo que contém o autômato

  Returns:
    automato (Automato): o automato presente no arquivo

  """
  f = open(caminho, 'r')
  linhas = f.read().split('\n')

  estados, inicial, aceitacao = linhas[:3]
  estados = estados[len("estados "):]
  estados = estados.split(', ')

  inicial = inicial[len("inicial "):]

  aceitacao = aceitacao[len("aceita "):]
  aceitacao = aceitacao.split(', ')

  transicoes = linhas[3:]
  transicoes.pop()
  transicoes = map(converte_transicao, transicoes)

  automato = Automato(estados, inicial, aceitacao, transicoes)

  return automato

def imprimir_automato(automato):
  print("\n----AUTOMATO----")
  print("Estados: %s" % automato.estados)
  print("Estado inicial: %s" % automato.estado_inicial)
  print("Estados de aceitação: %s" % automato.estados_aceitacao)
  print("Transições:")
  for transicao in automato.transicoes:
      print(transicao)