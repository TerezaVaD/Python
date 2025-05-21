import random

min_hodnota = 1
max_hodnota = 6
while True:
    print("Hazim kostkou...")
    kostka_hodnota = random.randint(min_hodnota,max_hodnota)
    print("Na kostce je",kostka_hodnota)
    if kostka_hodnota == 6:    
        continue
    else:
        break

