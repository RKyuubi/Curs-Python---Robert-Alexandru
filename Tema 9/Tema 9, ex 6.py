lista1=[] #se introduce orice lista
lista2=[] #se introduce orice lista

set1 = set(lista1)
set2 = set(lista2)

print(set1 & set2)

#elemente diferite doar din lista 1
print(set1 - set2)

#elemente diferite doar din lista 2
print(set2 - set1)

#elemente unice
print(set1 ^ set2)

