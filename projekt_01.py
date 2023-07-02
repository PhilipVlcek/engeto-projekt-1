"""

projekt_01.py: první projekt do Engeto Online Python Akademie

author: Filip Vlček
email: philip.vlcek@seznam.cz
discord: Filip_#8786

"""

import task_template

delici_cara = "\n" + "-" * 79 + "\n"

registrovani = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

seznam_registrovanych = list(registrovani.items())

print(delici_cara)

zadane_jmeno = input("Username: ")
zadane_heslo = input("Password: ")

if zadane_jmeno.lower() == seznam_registrovanych[0][0] and zadane_heslo == seznam_registrovanych[0][1]:
    print(delici_cara)
    print(f"Welcome to the app, {seznam_registrovanych[0][0]} \n-> We have 3 texts to be analyzed.")

elif zadane_jmeno.lower() == seznam_registrovanych[1][0] and zadane_heslo == seznam_registrovanych[1][1]:
    print(delici_cara)
    print(f"Welcome to the app, {seznam_registrovanych[1][0]} \n-> We have 3 texts to be analyzed.") 

elif zadane_jmeno.lower() == seznam_registrovanych[2][0] and zadane_heslo == seznam_registrovanych[2][1]:
    print(delici_cara)
    print(f"Welcome to the app, {seznam_registrovanych[2][0]} \n-> We have 3 texts to be analyzed.") 

elif zadane_jmeno.lower() == seznam_registrovanych[3][0] and zadane_heslo == seznam_registrovanych[3][1]:
    print(delici_cara)
    print(f"Welcome to the app, {seznam_registrovanych[3][0]} \n-> We have 3 texts to be analyzed.")

else:
    print(delici_cara)
    print("Unregistered user, terminating the program..")
    quit()   

print(delici_cara)

zadane_cislo = int(input("Enter a number to select text (1-3): "))

index_textu = None

if zadane_cislo == 1:
    index_textu = 0
elif zadane_cislo == 2:
    index_textu = 1
elif zadane_cislo == 3:
    index_textu = 2
else:
    print(delici_cara)
    print("Incorrect number")
    quit()

text = task_template.TEXTS[index_textu].split()

zvoleny_text = []

for slovo in text:
    zvoleny_text.append(slovo.strip(".,:;"))

prvni_velke = []
cele_velke = []
cele_male = []
cisla = []

for slovo in zvoleny_text:

    if slovo.isnumeric():
        cisla.append(int(slovo))

    elif slovo.isupper():
        cele_velke.append(slovo)

    elif slovo.istitle():
        prvni_velke.append(slovo)

    elif slovo.islower():
        cele_male.append(slovo)

    else:
        continue

print(f"""
There are {len(zvoleny_text)} words in the selected text.
There are {len(prvni_velke)} titlecase words.
There are {len(cele_velke)} uppercase words.
There are {len(cele_male)} lowercase words.
There are {len(cisla)} numeric strings.
The sum of all the numbers {sum(cisla)}.
""")

print(delici_cara)

pismena = []
mezera = None

cara = "-" * 30

for slovo in zvoleny_text:
    pismena.append(len(slovo))

print(f"\nLEN |  OCCURENCES       | NR. \n{cara}")
for cislo in range(min(pismena), max(pismena) + 1):

    hvezdicky = "*" * pismena.count(cislo)

    if cislo <= 9:
        mezera = " " * 2
    else:
        mezera = " "

    mezera_2 = " " * (17 - len(hvezdicky))

    print(f" {cislo}{mezera}|  {hvezdicky}{mezera_2}| {pismena.count(cislo)}")




