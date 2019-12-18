#NyGGa39
#Data utworzenia: 17.12.2019 r.
#Bez samoglosek

message = input ("Wprowadz komunikat: ")
new_message = ""
SAMOGLOWSKI = "aąeęiouy"

print()
for letter in message:
    if letter.lower() not in SAMOGLOWSKI:
        new_message += letter
        print ("\nZostal utworzony nowy lancuch: ", new_message)

print ("\nTwoj komunikat bez samoglosek to: ", new_message)

input ("\n\n\nAby zakonczyc wcisnij enter")
