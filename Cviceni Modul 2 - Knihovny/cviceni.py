import random

moznosti = ['kamen','nuzky','papir']
hrac = 'kamen'
pocitac = random.choice(moznosti)

if pocitac == 'kamen':
    print("PC ma",pocitac,"a ty kamen. Remiza")
elif pocitac == 'nuzky':
    print("PC ma",pocitac,"a ty kamen. Vyhral jsi")
else:
    print("PC ma",pocitac,"a ty kamen. Prohral jsi")