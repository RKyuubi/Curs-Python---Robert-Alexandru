def returneaza_tip_fisier(fisier):
    """
    Returneaza tipul fisierului introdus
    """
    pozitie_punct = fisier.rfind(".")
    extensie_fisier = ""
    if pozitie_punct != -1:
        extensie_fisier = fisier[pozitie_punct + 1:]

    if extensie_fisier =="jpg":
        return "Fisierul introdus este imagine"
    elif extensie_fisier =="mp3":
        return "Fisierul introdus este muzica"
    elif extensie_fisier =="txt":
        return "Fisierul introdus este text"
    else:
        return "Tip fisier necunoscut sau fara extensie valida."

fisier = input("Introduceti orice fisier: ")
print (returneaza_tip_fisier(fisier))
