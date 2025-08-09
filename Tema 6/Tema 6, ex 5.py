numar = int(input("Introduceti orice numar de 4 cifre:"))
numar += 1 #plecam de la numar+1 deoarece avem nevoie sa verificam de la urmatorul numar

while True:
    if numar > 9999:
        print ("Nu mai este numar de 4 cifre")
        break

    cifre_numar =str(numar)
    lista_cifre = []
    cifra_diferita = True

    for cifra in cifre_numar:
        if cifra in lista_cifre:
            cifra_diferita = False
            break
        else:
            lista_cifre.append(cifra)

    if cifra_diferita is True:
        numar_nou ="".join(lista_cifre)
        print(f"\nUrmatorul cel mai mic numar de 4 cifre diferite este",numar_nou)
        break

    else:
        numar += 1