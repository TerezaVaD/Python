import os

jmena_slozek = ("obrazky","texty","gify")

for jmeno in jmena_slozek:
    # pokud soubor existuje a je to složka, přeskoč jej
    if os.path.exists(jmeno) and os.path.isdir(jmeno):
        print("Složka již existuje!")

    # .. jinak ji vytvoř
    else:
        print("Tvořím novou složku:", jmeno)
        os.mkdir(jmeno)

# jakmile budou všechny složky vytvořené, vypiš oznámení
print("Všechny složky existují")