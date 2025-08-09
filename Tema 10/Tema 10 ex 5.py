def cuvinte_unice (cuvant):
    """
    Returneaza True sau False daca un cuvant contine litere care nu se repeta
    """
    cuvant_litere_mici = cuvant.lower()
    if len(set(cuvant_litere_mici)) == len(cuvant_litere_mici):
        return (f"{True} \nCuvantul '{cuvant}' contine litere care NU se repeta")
    else:
        return (f"{False} \nCuvantul '{cuvant}' contine litere care se repeta")

cuvant = input("Introduceti orice cuvant:")
print (cuvinte_unice(cuvant))
