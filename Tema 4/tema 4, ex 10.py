numarul = int(input("introduceti orice numar:"))
suma = 0

while numarul != 0:
    suma += numarul % 10
    numarul //= 10
    print (numarul,suma)
