#NyGGa39
#Data utworzenia: 02.12.2019r.
#Zgadnij jaka to liczba

import random

print("Witaj. \nZagramy w małą grę. \nPomysle o pewnej liczbie od 1 do 100, \
a Ty sprobuj w jak najmniejszej liczbie prob odgadnac jaka to liczba.")

the_number = random.randint(1, 100)
guess = int(input("Podaj liczbe: "))
tries = 1

while guess != the_number:
    if guess > the_number:
        print("Za duza...")
    else:
        print("Za mala...")
    guess = int(input("Podaj liczbe: "))
    tries += 1

while guess == the_number:
    print("Gratulacje! Odgadles liczbe! Ta liczba to: ", the_number)
    print("Potrzebowales/as tylko ", tries, " prob!")
    break




input("Wcisnij enter, aby zakonczyc")