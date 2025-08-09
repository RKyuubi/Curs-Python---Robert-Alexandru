def suma_numere_din_string(string1):
    """
    Calculeaza suma numerelor dintr-un string
    """
    suma_numere = 0
    lista1 = string1.split()
    for cuvant in lista1:
        if cuvant.isdigit():
            suma_numere += int(cuvant)
    return suma_numere

print(suma_numere_din_string(input("Introduceti orice propozitie: ")))