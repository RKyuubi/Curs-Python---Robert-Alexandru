if __name__ =='__main__':
    lista1 = [2,3,4,5]
    lista2 = [6,7,8,9]

    lista1x2 = list(map(lambda x, y: x*y, lista1, lista2))
    print(lista1x2)