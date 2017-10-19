#Aula 11 - Strings

# Vetor de caracteres
x = "Churros"

print("Zabumba")

#.capitalize() = Transforma a primeira letra em caixa alta
x = "churros"
print(x.capitalize())
print(x)

#.replace("x", "y") substitui x por y
print(x.replace("ch", "b"))

#.isalpha() = Se é alfanumérico (números)
print(x.isnumeric())

#.split(",") = Separa, em um vetor, os valores que estão entre vírgulas.
nomes = "Jonas,Chico Bioca,Jailson,Paulo Guina,Cauã"
print(nomes.split(",")[2])

#"HAgs {0} dfjkhdf {1}.format("x", "y") - Substitui os dados de acordo com a ordem.
print("A mãe do {0} é {1}".format("Fulano", "muito gorda"))

# ou pode usar f"odjsdjhjf {x} sadhf {y}"

fulano = "Zeca"
elogio = "muito gorda"

print(f"A mãe do {fulano} é {elogio}")