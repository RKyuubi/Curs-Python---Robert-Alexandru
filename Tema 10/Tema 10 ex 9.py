def lista_comparatii_numere (lista):
    """
    Returneaza intr-o lista noua cate numere din cadrul listei initiale sunt mai mici decat elementul i
    """
    lista_caractere = []
    for caracter in lista:
        if caracter.isdigit():
            lista_caractere.append(caracter)
            
    lista_rezultate = []
    for element_curent in lista_caractere:
        contor_comparatie = 0
        for element_comparat in lista_caractere:
            if element_curent.isdigit() and element_comparat.isdigit() and int(element_curent) > int(element_comparat):
                contor_comparatie += 1
        lista_rezultate.append(contor_comparatie)

    return lista_rezultate

lista = input("Introduceti orice lista formata din numere intregi pozitive: ")
print (lista_comparatii_numere(lista))