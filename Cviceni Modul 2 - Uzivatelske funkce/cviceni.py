prvni_cislo = 5
druhe_cislo = 5

def vynasob(num1,num2):
    return num1*num2

vysledek = vynasob(5,6)
print(vysledek)


vstupni_text = 'Ahoj všem, tady Engeto'

def zdvojnasob_znaky(text):
    zdvojene = list()
    for znak in text:
        zdvojene.append(znak*2)
    return "".join(zdvojene)

vysledek2 = zdvojnasob_znaky(vstupni_text)
print(vysledek2)

prvni_cislo = 12
druhe_cislo = 16

def najdi_gcd(x1: int,x2:int) -> int:
    while x2 > 1:
        zbytek_po_deleni = x1 % x2

        if not zbytek_po_deleni:
            break

        x1, x2 = x2, zbytek_po_deleni
    return x2

# Najdi největšího společného dělitele a ulož jej do proměnné
vysledek = najdi_gcd(prvni_cislo, druhe_cislo)

# Tisk výsledku
print(vysledek)

import random
from statistics import mean

nahodna_cisla = []


nahodna_cisla = [random.randint(1, 100) for _ in range(10)]

print(nahodna_cisla)
prumer = mean(nahodna_cisla)

print("Prumer nahodnych cisel je: ", prumer)