import unittest

from GNC import GeradorNomeCachaceiro

class test_GNC(unittest.TestCase):

    def test_criar_objeto_gerador_nome_cachaceiro(self):
        gnc = GeradorNomeCachaceiro()