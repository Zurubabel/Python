"""
    Aula 15 - Ifs, elses, elifs e booleanos

"""

# == Igual
# != Diferente
# >= Maior OU Igual
# > Maior
# <= Menor OU Igual
# < Menor

# print(1 == 1)

# print("Zé" == "Zé")

# if (decisão):
#    escopo do if se o valor for verdadeiro

#churros = 10

#if churros == 10:
#    print("Churros é igual a 10")

dinheiro = 35

#mequidonaudis = 55

#if dinheiro - mequidonaudis > 0:
#    print("Posso comer de boas que ainda tenho dinheiro pra voltar pra casa")
#else:
#    print("Ferrou! Vou dormir no shópis")

biguimequi = 26
shedar = 26
uoper = 23

if biguimequi < shedar:
    print("Compro o Biguimequi")
elif shedar < biguimequi:
    print("Compro o Shedar")
elif uoper < (0.8 * biguimequi):
    print("Vô cumê no Bugueking")
else:
    print("Vo cume nada. Vo cumê em casa")