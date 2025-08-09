lista1 = [12, "eu", 10.3, "asdasda", 1,3,4,5]
lista2 = []

for char in lista1:
    if type(char) == int or type(char) == float:
        lista2.append(char)

print(max(lista2))