"""
    Aula 16 - Operadores Lógicos e sua ordem

    and - E
    or - OU
    not - NÃO

"""

cancro = False
sarampo = False
catapora = True
variola = True
hepatite = True
gastrite = True
conjutivite = True

if (sarampo or catapora) and cancro:
    print("Doença transmissível")
else:
    print("Doença 'de boas'")

#if not (sarampo or variola or hepatite):
#    print("3 doenças")
#else:
#    print("0 doenças")

# NOT
#if cancro and not sarampo:
#    print("Tu não é tão doente")
#else:
#    print("Tu ainda é doente pra cacete")

# AND
#if cancro and sarampo and variola:
#    print("Tu é doenchi")
#else:
#    print("Tu não é tão doente")

# OR
#if cancro or sarampo or catapora:
#    print("Tu é doenchi")
#else:
#    print("Tu não é tão doente")
