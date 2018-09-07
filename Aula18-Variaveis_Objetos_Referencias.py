"""
    Aula 18 - Variáveis, Objetos e Referências

"""

x = 1
y = "4"
print("endereço x = {}".format(id(x)))
print("endereço y = {}".format(id(y)))

x = y

print("endereço x = {}".format(id(x)))
print(type(x))

#print(id(y))

#1842530032