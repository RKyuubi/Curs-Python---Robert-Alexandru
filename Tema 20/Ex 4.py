if __name__ == "__main__":
    lista_prenume = ["Ion", "Maria", "Andrei"]
    lista_nume = ["Popescu", "Ionescu", "Georgescu"]

    lista_nume_complet = list(map(lambda x, y: f'{x} {y}', lista_prenume, lista_nume))
    print(lista_nume_complet)