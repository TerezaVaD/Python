# Scraper volebních výsledků z roku 2017

Tento projekt slouží k automatickému stahování a zpracování volebních výsledků z webu volby.cz za rok 2017. Scraper získává údaje o počtu voličů, vydaných obálkách, platných hlasech a výsledcích jednotlivých politických stran pro každou obec.

## Instalace

1. **Vytvoření virtuálního prostředí:**
   Nejprve je doporučeno vytvořit virtuální prostředí pro tento projekt, aby byly všechny knihovny izolovány od ostatních projektů.
   
   - Na Windows:
     '''bash
     python -m venv venv
     .\venv\Scripts\activate
     '''
   
   - Na MacOS/Linux:
     '''bash
     python3 -m venv venv
     source venv/bin/activate
     '''

2. **Instalace knihoven:**
   Jakmile je virtuální prostředí aktivováno, nainstaluj potřebné knihovny pomocí 'requirements.txt':
   
   '''bash
   pip install -r requirements.txt

3. **Spuštění projektu:**

Skript se spustí pomocí příkazu:
python main.py <URL> <výstupní_soubor.csv>


Kde:

<URL> je URL stránky s odkazy na jednotlivé obce, např. https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101.

<výstupní_soubor.csv> je název CSV souboru, do kterého budou výsledky uloženy (např. vysledky.csv).

Příklad spuštění:

Představme si, že chcete získat výsledky pro kraj s kódem 2 a obce v něm. Příkaz by mohl vypadat takto:
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" vysledky.csv

Výstup:

Výstupní soubor bude obsahovat následující sloupce:

Code: Kód obce

Location: Název obce

Registered: Počet registrovaných voličů

Envelopes: Počet vydaných obálek

Valid: Počet platných hlasů

Následně pro každou politickou stranu budou uvedeny hlasy.

