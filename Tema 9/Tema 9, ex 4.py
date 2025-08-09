numar = int(input("Introduceti orice numar de 4 cifre:"))
numar += 1 #plecam de la numar+1 deoarece avem nevoie sa verificam de la urmatorul numar

while True:
    if numar > 9999:
        print ("Nu mai este numar de 4 cifre")
        break

    cifre_numar =str(numar)
    set_cifre = set(cifre_numar)

    if len(set_cifre) == len(cifre_numar):
        print (f"Urmatorul cel mai mic numar de 4 cifre este:{numar}")
        break

    else:
        numar += 1