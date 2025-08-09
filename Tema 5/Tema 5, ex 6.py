string_1 = input ("Introduceti primul string:")
string_2 = input ("Introduceti al doilea string:")
lista = []
nr_caractere_comune = 0

string_1 = string_1.lower()
string_2 = string_2.lower()

for char in string_1:
    if char in string_2 and char.isalpha() and char not in lista:
        lista.append(char)
        nr_caractere_comune += 1

print ("\nCaracterele comune sunt:", lista)
print ("Numarul de caractere comune este:", nr_caractere_comune)