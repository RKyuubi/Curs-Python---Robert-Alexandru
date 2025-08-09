def contor_nume(nume):
    numar_nume = 0
    with open("Nume", "r") as fisier:
        lista = fisier.readlines()
        for element in lista:
            if element.strip() == nume:
                numar_nume += 1
    print (numar_nume)

def contor_nume_2():
    dictionar_nume = {}
    with open("Nume", "r+") as fisier:
        lista_nume = fisier.read().split()
        # print(lista_nume)
        for nume in lista_nume:
            if nume in dictionar_nume:
                dictionar_nume[nume] += 1
            else:
                dictionar_nume[nume] = 1
        fisier.write(str(dictionar_nume))
    # print(dictionar_nume)

        # print(input_fisier.split())
        # for element in lista:
        #     if element.strip() == nume:
        #         numar_nume += 1
    # print (numar_nume)

if __name__ == "__main__":
    contor_nume_2()
