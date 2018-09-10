# 1 - Armazenar os nomes e apelidos de cachaceiros
# 2 - Mês e o dia da pessoa

# mês - 1 até 12
# dia - 1 até 31
#mes = 11
#dia = 15

#retorno = ""

# Mes - nome; Dia - apelido


class GeradorNomeCachaceiro:

    def __init__(self):
        self.nomes = ["Betinho", "Xexéu", "Zé", "Chicão", "Elias", "Ribamar",
                 "Arlindo", "Sérgio", "Tião", "Bibica", "Bira", "Zeca"]

        self.apelidos = ["Furico", "da Viola", "rosca solta", "Frasqueira", "Gambá", "Kokin", "Punheteiro",
                    "Ku de Largata", "Doido", "Meu Mel", "Babaçu", "Carcaça trepada", "Alma Penada",
                    "O crente das pinga", "das Mandingas", "cai torto", "chifrudo", "bola murcha", "do goró",
                    "cana brava", "Macumbeiro", "171", "corno manso", "Bala Choca", "Freadão",
                    "Vaca véia", "Nega Balaio", "Rola Cansada", "só cana", "Caganeira", "Ku de Mel"]

    def retornar_nome(self, numero_mes):
        return self.nomes[numero_mes - 1]

# Decisão de qual nome retornar
"""if mes == 1:
    retorno = jan
elif mes == 2:
    retorno = fev
elif mes == 3:
    retorno = mar """

