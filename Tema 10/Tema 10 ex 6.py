def numar_suma_descompus (numar):
    """
    Returneaza numarul ca string in format de suma
    """
    lista = []
    putere_a_lui_10 = 1
    numar_temporar = numar
    while numar_temporar > 0:
        cifra_curenta = numar_temporar % 10
        valoare_pozitionala = cifra_curenta*putere_a_lui_10
        if valoare_pozitionala != 0:
            lista.append(str(valoare_pozitionala))
        numar_temporar //= 10
        putere_a_lui_10 *=10

    lista.reverse()
    return "+".join(lista)

numar = int(input("Introduceti orice numar:"))
print(numar_suma_descompus(numar))