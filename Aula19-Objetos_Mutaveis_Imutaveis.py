"""
    Aula 19 - Dados mutáveis e imutáveis
"""
# Imutável
#x = 1
#print(id(x))
#x += 3
#print(id(x))

#Mutável

x = []
print(id(x))
print(x)
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.append(5)
x.append(6)
print(id(x))
print(id(x[0]))
print(id(x[1]))
print(id(x[2]))


