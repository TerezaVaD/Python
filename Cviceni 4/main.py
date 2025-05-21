'''
zadany_slovnik = {
   'jmeno':'Pepa',
   'prijmeni': 'Novak',
   'rok_narozeni': 1990,
   'email': 'pepa.novak@seznam.cz'
}

def obsahuje_udaje(klic,hodnota,slovnik):
  if klic in slovnik:  
    print(f"Klíč: {klic} nalezen")
    if slovnik[klic] == hodnota:
        return True
    else:
        print(f"Klíč: {klic} nenalezen")
        return False
    
  else:
      vysledek = False
      print(f"Hodnota: {hodnota} nenalezena")
    
  return vysledek

vystup_1 = obsahuje_udaje("jmeno","Pepa",zadany_slovnik)
vystup_2 = obsahuje_udaje("jmeno","Marek",zadany_slovnik)
vystup_3 = obsahuje_udaje("name","John",zadany_slovnik)

print(vystup_2)
'''

# bez knihovny nemůžeš pracovat s JSON objekty
import json
'''
chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# funkci 'open' nachystáš objekt v Pythonu
json_soubor = open("prvni_json_soubor.json", mode="w")

# metoda 'dump' uloží objektu do souboru
json.dump(chuckuv_slovnik, json_soubor)

# ... nezapomeň objekt ukončit
json_soubor.close()

'''

import csv

'''
hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]

# ... nachystáš nový soubor pro zápis
nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")

# ... vytvoříš zapisovací objekt, který do souboru zapíše údaje
zapisovac = csv.writer(nove_csv)

# ... nejprve zapíšeš záhlaví
zapisovac.writerow(hlavicka)

# ... potom první údaj
zapisovac.writerow(osoba_1)

# ... druhý údaj
zapisovac.writerow(osoba_2)

# ... nakonec objekt a soubor uzavřeš
nove_csv.close()
'''


hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]

nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")

zapisovac = csv.writer(nove_csv)
zapisovac.writerows(
   ( 
       hlavicka,
       osoba_1,
       osoba_2
   )
)
nove_csv.close()