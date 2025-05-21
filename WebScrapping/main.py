import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://heroes3.cz/hraci/index.php?page=1&order=0&razeni=DESC"
vystupni_soubor = "vystup_tab_1.csv"

odp_serveru = requests.get(url)

#print(odp_serveru.text)

#print(odp_serveru.text[1:16])

soup = BeautifulSoup(odp_serveru.text,'html.parser')
#print(soup.prettify())

table_tag_top = soup.find("table",{"class":"tab_top"})
#print(table_tag_top)

vsechny_tr = table_tag_top.find_all("tr")
#print(vsechny_tr)

for tr in vsechny_tr[1:]:
    td_na_radku = tr.find_all("td")
    print(td_na_radku[2].get_text())

def vyber_atributy_z_radku(tr_tag:"bs4.element.ResultSet"):
    
    return {
        "poradi":tr_tag[0].getText(),
        "jmeno":tr_tag[2].getText(),
        "vitezstvi":tr_tag[5].getText(),
        "celkem_her":tr_tag[6].getText()
    }

vysledky = []
for tr in vsechny_tr[1:]:
    td_na_radku = tr.find_all("td")
    data_grace = vyber_atributy_z_radku(td_na_radku)
    vysledky.append(data_grace)

pprint(f"VYSLEDKY: {vysledky}")