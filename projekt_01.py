"""

projekt_01.py: první projekt do Engeto Online Python Akademie

author: Filip Vlček
email: philip.vlcek@seznam.cz
discord: Filip_#8786

"""

import task_template

dividing_line = "\n" + "-" * 79 + "\n"

registered = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

print(dividing_line)

Username = input("Username: ")
Password = input("Password: ")

if Username in registered and Password == registered[Username]:
    print(dividing_line)
    print(f"Welcome to the app, {Username} \n-> We have 3 texts to be analyzed.")
else:
    print(dividing_line)
    print("Unregistered user, terminating the program..")
    quit()   

print(dividing_line)

number = input("Enter a number to select text (1-3): ")

if number.isnumeric() and int(number) in range(1, 4):
    (text_index := int(number) - 1)
    print(dividing_line)
else:
    print(dividing_line)
    print("Incorrect number")
    quit()

text = task_template.TEXTS[text_index].split()

selected_text = []

for word in text:
    selected_text.append(word.strip(".,:;"))

title_letter = []
uppercase = []
lowercase = []
numbers = []

for word in selected_text:

    if word.isnumeric():
        numbers.append(int(word))

    elif word.isupper():
        uppercase.append(word)

    elif word.istitle():
        title_letter.append(word)

    elif word.islower():
        lowercase.append(word)

    else:
        continue

print(f"""
There are {len(selected_text)} words in the selected text.
There are {len(title_letter)} titlecase words.
There are {len(uppercase)} uppercase words.
There are {len(lowercase)} lowercase words.
There are {len(numbers)} numeric strings.
The sum of all the numbers {sum(numbers)}.
""")

print(dividing_line)

letters = []
space = None

line = "-" * 30

for word in selected_text:
    letters.append(len(word))

print(f"\nLEN |  OCCURENCES       | NR. \n{line}")
for number in range(min(letters), max(letters) + 1):

    stars = "*" * letters.count(number)

    if number <= 9:
        space = " " * 2
    else:
        space = " "

    space_2 = " " * (17 - len(stars))

    print(f" {number}{space}|  {stars}{space_2}| {letters.count(number)}")




