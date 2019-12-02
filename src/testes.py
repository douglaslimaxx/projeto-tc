import unittest
from classes import *
from operacoes import *
from verificador import *


class Test(unittest.TestCase):

    def test_complemento(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", 0, "B"), Transicao("A", 1, "A"), Transicao("B", 1, "B"), Transicao("B", 0, "A")])
            
        automato_resultante = complemento(automato1)
        automato_esperado = Automato(["A", "B"], "A", ["A"], [Transicao(
            "A", 0, "B"), Transicao("A", 1, "A"), Transicao("B", 1, "B"), Transicao("B", 0, "A")])

        self.assertEqual(automato_esperado,automato_resultante)

    def test_aceita_afd(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "B"), Transicao("A", "1", "A"), Transicao("B", "1", "B"), Transicao("B", "0", "A")])
    
        self.assertEqual(verifica(automato1,"101"),True)

    def test_rejeita_afn(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "B"), Transicao("A", "1", "A"), Transicao("B", "1", "B"), Transicao("B", "0", "A")])
    
        self.assertEqual(verifica(automato1,"1001"),0)

    def test_aceita_afn(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "A"), Transicao("A", "1", "A"), Transicao("A", "1", "B")])
    
        self.assertEqual(verifica(automato1,"10010"),0)
    """
    0*1*
    """
    def test_aceita_afn_e(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "A"), Transicao("A", "e", "B"), Transicao("B", "1", "B")])
    
        self.assertEqual(verifica(automato1,"0000011111"),1)

    def test_rejeita_afn_e(self):
        automato1 = Automato(["A", "B"], "A", ["B"], [Transicao(
            "A", "0", "A"), Transicao("A", "e", "B"), Transicao("B", "1", "B")])
    
        self.assertEqual(verifica(automato1,"1111111011"),0)

    
    




if __name__ == '__main__':
    unittest.main()
