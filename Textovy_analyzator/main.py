"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tereza Dostalíková
email: tereza.dostalikova@icloud.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
# overeni prihlasovacich udaju
users = {"bob":"123","ann":"pass123","mike":"password123","liz":"pass123"}
login = input("Username: ")
password = input("Password: ")
print("-" * 30)

if login in users and users[login] == password:
    print("Welcome to the app,",login,"\nWe have 3 texts to be analyzed.")
    print("-" * 30)
else:
    print("Unregistered user, terminating the program..")
    exit()

# zadani cisla textu a overeni, zda neni zadana jina hodnota nez cislo (osetreno try-except)
# resp zda je zadane cislo 1-3
try:
    number = int(input("Enter a number btw. 1 and 3 to select: "))
except ValueError:
    print("This is not number, terminating the program..")
    exit()
if number > 3 or number < 1:
    print("Out of range, terminating the program..")
    exit()

# jednotlive operace s textem
print("-" * 30)
selected_text = TEXTS[number-1]
titlecase_words = [word for word in selected_text.split() if word[0].isupper()]
uppercase_words = [word for word in selected_text.split() if word.isupper()]
lowercase_words = [word for word in selected_text.split() if word.islower()]
numeric_strings = [word for word in selected_text.split() if word.isdigit()]
print(f"There are {len(selected_text.split())} words in the selected text")
print(f"There are {len(titlecase_words)} titlecase words.")
print(f"There are {len(uppercase_words)} uppercase words.")
print(f"There are {len(lowercase_words)} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print("The sum of all the numbers",sum(list(map(int,numeric_strings))))

# priprava jednoducheho grafu, stanoveni sire sloupcu pro lepsi prehlednost grafu
words_lenght = [len(word) for word in selected_text.split()]

col1_width = 3
col2_width = 12
col3_width = 3

# hlavicka grafu
print("-" * 30)
print(f"{'LEN':<{col1_width+2}} | {'OCCURENCES':<{col2_width+3}} | {'NR.':<{col3_width}}")
print("-" * 30)

# vypsani samotneho grafu
for i in range(1,max(words_lenght)+1):
    if words_lenght[i]>0:
        print(f"{i:<{col1_width}}   | {'*' * words_lenght[i]:<{col2_width}}    | {words_lenght[i]:<{col3_width}}")
