import unittest

from GNC import GeradorNomeCachaceiro


class GNCTest(unittest.TestCase):

    def setUp(self):
        nomes = ["Betinho", "Xexéu", "Zé", "Chicão", "Elias", "Ribamar",
                "Arlindo", "Sérgio", "Tião", "Bibica", "Bira", "Zeca"]

        apelidos = ["Furico", "da Viola", "rosca solta", "Frasqueira", "Gambá", "Kokin", "Punheteiro",
                    "Ku de Largata", "Doido", "Meu Mel", "Babaçu", "Carcaça trepada", "Alma Penada",
                    "O crente das pinga", "das Mandingas", "cai torto", "chifrudo", "bola murcha", "do goró",
                    "cana brava", "Macumbeiro", "171", "corno manso", "Bala Choca", "Freadão",
                    "Vaca véia", "Nega Balaio", "Rola Cansada", "só cana", "Caganeira", "Ku de Mel"]

        self.gnc = GeradorNomeCachaceiro(nomes, apelidos)

    def tearDown(self):
        pass

    def test_quantidade_de_nomes_e_igual_a_doze(self):
        self.assertEqual(12, len(self.gnc.nomes))

    def test_quantidade_de_apelidos_e_igual_a_trinta_e_um(self):
        self.assertEqual(31, len(self.gnc.apelidos))

    def test_retornar_nome_ao_inserir_numero_do_mes_do_aniversario_do_usuario(self):
        self.assertEqual(self.gnc.retornar_nome(1), "Betinho")

    def test_retornar_apelido_ao_inserir_dia_do_aniversario_do_usuario(self):
        self.assertEqual(self.gnc.retornar_apelido(1), "Furico")