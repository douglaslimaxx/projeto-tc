import unittest
from classes import *
from operacoes import *
from verificador import *


class Test(unittest.TestCase):

    def test_aceita_afd(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "B"), Transicao("A", "1", "A"), Transicao("B", "1", "B"), Transicao("B", "0", "A")])

        self.assertEqual(verifica(automato1, "101"), True)

    def test_rejeita_afn(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "A"), Transicao("A", "1", "A"), Transicao("A", "1", "B")])
        self.assertEqual(verifica(automato1, "1001000"), 0)

    def test_aceita_afn(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "A"), Transicao("A", "1", "A"), Transicao("A", "1", "B")])

        self.assertEqual(verifica(automato1, "1001"), 1)
    """
    0*1*
    """

    def test_aceita_afn_e(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "A"), Transicao("A", "e", "B"), Transicao("B", "1", "B")])

        self.assertEqual(verifica(automato1, "0000011111"), 1)

    def test_rejeita_afn_e(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "A"), Transicao("A", "e", "B"), Transicao("B", "1", "B")])

        self.assertEqual(verifica(automato1, "1111111011"), 0)
        self.assertEqual(verifica(automato1, "00111000"), 0)

    def test_complemento(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", 0, "B"), Transicao("A", 1, "A"), Transicao("B", 1, "B"), Transicao("B", 0, "A")])

        automato_resultante = complemento(automato1)
        automato_esperado = Automato(["A", "B"], "A", ["A"], [Transicao(
            "A", 0, "B"), Transicao("A", 1, "A"), Transicao("B", 1, "B"), Transicao("B", 0, "A")])

        self.assertEqual(automato_esperado, automato_resultante)

    def test_uniao(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "B"), Transicao("A", "1", "A"), Transicao("B", "1", "B"), Transicao("B", "0", "A")])
        automato2 = Automato(["C", "D"], "C", ["D"], [Transicao(
            "C", "1", "D"), Transicao("C", "0", "C"), Transicao("D", "0", "D"), Transicao("D", "1", "C")])

        automato_resultante = uniao(automato1, automato2)
        automato_esperado = Automato(["A", "B", "C", "D", "NOVO"], "NOVO", ["B", "D"], [Transicao(
            "A", "0", "B"), Transicao("A", "1", "A"), Transicao("B", "1", "B"), Transicao("B", "0", "A"), Transicao(
            "C", "1", "D"), Transicao("C", "0", "C"), Transicao("D", "0", "D"), Transicao("D", "1", "C"), Transicao("NOVO", "e", "A"), Transicao("NOVO", "e", "C")])
        self.assertEqual(automato_esperado, automato_resultante)
       

    def test_estrela(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "B"), Transicao("A", "1", "A"), Transicao("B", "1", "B"), Transicao("B", "0", "A")])
        automato_esperado = Automato(["A", "B", "NOVO"], "NOVO", ["B", "NOVO"], [Transicao(
            "A", "0", "B"), Transicao("A", "1", "A"), Transicao("B", "1", "B"), Transicao("B", "0", "A"), Transicao("NOVO", "e", "A"), Transicao("B", "e", "A")])

        automato_resultante = estrela(automato1)
        self.assertEqual(automato_esperado, automato_resultante)

    def test_intersecao(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "B"), Transicao("A", "1", "A"), Transicao("B", "1", "B"), Transicao("B", "0", "A")])
        automato2 = Automato(["C", "D"], "C", ["D"], [Transicao(
            "C", "1", "D"), Transicao("C", "0", "C"), Transicao("D", "0", "D"), Transicao("D", "1", "C")])
        automato_resultante = intersecao(automato1, automato2)
        automato_esperado = Automato(["BD", "BC", "AD", "AC"], "AC", ["BD"], [Transicao(
            "AC", "0", "BC"), Transicao("AD", "0", "BD"), Transicao("AC", "1", "AD"), Transicao("AD", "1", "AC"), Transicao(
            "BC", "1", "BD"), Transicao("BD", "1", "BC"), Transicao("BC", "0", "AC"), Transicao("BD", "0", "AD")])
        self.assertEqual(automato_esperado, automato_resultante)


if __name__ == "__main__":
    unittest.main()




