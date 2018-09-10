import unittest

from GNC import GeradorNomeCachaceiro


class GNCTest(unittest.TestCase):

    def test_criar_objeto_gerador_nome_cachaceiro(self):
        gnc = GeradorNomeCachaceiro()

    # A quantidade de nomes = 12
    def test_quantidade_de_nomes_e_igual_a_doze(self):
        gnc = GeradorNomeCachaceiro()
        self.assertEqual(12, len(gnc.nomes))

    # A quantidade de apelidos = 31
    def test_quantidade_de_apelidos_e_igual_a_trinta_e_um(self):
        gnc = GeradorNomeCachaceiro()
        self.assertEqual(31, len(gnc.apelidos))

    def test_retornar_nome_ao_inserir_numero_do_mes(self):
        gnc = GeradorNomeCachaceiro()
        self.assertEqual(gnc.retornar_nome(1), "Betinho")