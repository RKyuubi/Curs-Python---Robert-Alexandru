def lista_argumente(*lista_date):
    """
    Returneaza o lista cu toate elementele argumentelor
    """
    lista1 = []
    for lista in lista_date:
        if isinstance(lista, list):
            for element in lista:
                lista1.append(element)
        else:
            print ("Argumentul nu este o lista")
    return lista1

