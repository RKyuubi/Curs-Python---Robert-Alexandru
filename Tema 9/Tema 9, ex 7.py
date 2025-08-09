string = input("Introdu orice sir de caractere:")

dictionar_frecvente = {}

for caracter in string:
    if caracter in dictionar_frecvente:
        dictionar_frecvente[caracter] += 1
    else:
        dictionar_frecvente[caracter] = 1

print (dictionar_frecvente)

lista_frecvente = dictionar_frecvente.values()

if len(set(lista_frecvente)) == 1:
    print("Nu trebuie eliminat niciun caracter intrucat frecventele caracterelor string-ului introdus sunt egale")
else:
    frecventa_frecventelor = {}
    for freq in lista_frecvente:
        if freq in frecventa_frecventelor:
            frecventa_frecventelor[freq] += 1
        else:
            frecventa_frecventelor[freq] = 1

print (frecventa_frecventelor) #am avut o idee cu frecventa frecventelor si anumite situatii in care avem doar doua tipuri si cu diferentele dintre frecvente, dar s-au amestecat ideile si am pierdut tot
