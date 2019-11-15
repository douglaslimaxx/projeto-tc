# coding: utf-8
from classes import *

def converte_transicao(raw):
  origem, destino, entrada = raw.split(' ')
  return Transicao(origem, entrada, destino)

def importa_automato(caminho):
  f = open(caminho, 'r')
  lines = f.read().split('\n')

  estados, inicial, aceitacao = lines[:3]
  estados = estados[len("estados "):]
  estados = estados.split(', ')

  inicial = inicial[len("inicial "):]

  aceitacao = aceitacao[len("aceita "):]
  aceitacao = aceitacao.split(', ')

  transicoes = lines[3:]
  transicoes.pop()
  transicoes = map(converte_transicao, transicoes)

  return Automato(estados, inicial, aceitacao, transicoes)
