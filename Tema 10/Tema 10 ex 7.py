def scor_cuvant (cuvant):
    """
    Calculează valoarea unui cuvânt, atribuind A=1, B=2, ..., Z=26.
    """
    valoare_totala = 0

    for litera in cuvant:
        litera_mare = litera.upper()
        if "A" <= litera_mare <= "Z":
            valoare_litera = (ord(litera_mare) - ord('A')) + 1
            valoare_totala += valoare_litera

    return valoare_totala

cuvant = input("Introduceti orice cuvant: ")
print(scor_cuvant(cuvant))