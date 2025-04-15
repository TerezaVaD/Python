"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Tereza Dostalíková
email: tereza.dostalikova@icloud.com
"""

import random
import time

start_time = time.time()
print("Hi there!")
print("-------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a Bulls&Cows game")
print("-------------------------------")

def generate_number():
    digits = list("123456789")
    first_digit = random.choice(digits)
    remaining_digits = list("0123456789")
    remaining_digits.remove(first_digit)
    secret_number = first_digit + "".join(random.sample(remaining_digits, 3))
    return secret_number

def is_valid_guess(guess):
    return (
        guess.isdigit() and  # Kontroluje, zda je vstup tvoren pouze cisly
        len(guess) == 4 and  # Musi mit presne 4 cislice
        len(set(guess)) == 4 and  # Cislice musi byt unikatni
        guess[0] != "0"  # Cislo nesmi zacinat nulou
    )

def evaluate_guess(origin, guess):
    bulls = 0
    cows = 0
    # Seznamy pro zaznamenani spravnych a nespravnych pozic. 
    # Sleduji, ktere cislice uz byly pouzity pro urceni bulls a cows.
    origin_used = [False] * 4
    guess_used = [False] * 4

    # Zjisteni bulls
    for i in range(4):
        if guess[i] == origin[i]:
            bulls += 1
            origin_used[i] = True
            guess_used[i] = True

    # Zjisteni cows (ale pouze pro nesprávné pozice)
    for i in range(4):
        if not guess_used[i]:  # Pokud jeste nevyuzito v bulls
            for j in range(4):
                if not origin_used[j] and guess[i] == origin[j]:  # Pokud cislo ve spravnem seznamu
                    cows += 1
                    origin_used[j] = True
                    break
    return bulls, cows

# Funkce pro hru
def main():
    secret_number = generate_number()  # Tajne cislo, ktere hrac hada
    attempts = 0  # Pocitadlo pokusu
    print("--------------------------------")

    while True:
        players_guess = input("Enter a number:")  # Tip hrace

        if not is_valid_guess(players_guess):  # Pokud neni tip platny
            print("Invalid input! Enter a unique 4-digit number.")
            continue

        attempts += 1  # Zvysi pocet pokusu
        bulls, cows = evaluate_guess(secret_number, players_guess)
        
        # Vytvoreni spravneho vystupu pro bulls a cows
        bulls_text = "bull" if bulls == 1 else "bulls"
        cows_text = "cow" if cows == 1 else "cows"
        
        print(f">>> {players_guess}")
        print(f"{bulls} {bulls_text}, {cows} {cows_text}")
        print("--------------------------------")

        if bulls == 4:  # Pokud hrac uhodl cele cislo
            end_time = time.time()  # Ulozi cas konce hry
            final_time = round(end_time - start_time, 2)  # Spocita uplynuly čas
            print(f"Congratulations! You guessed the number correctly in {attempts} attempts and {final_time} seconds.")  
            break

if __name__ == "__main__":  
    main()  


