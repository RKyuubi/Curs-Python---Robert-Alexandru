cuvant = input ("Introduceti orice cuvant:")
dict1 = {}
for litera in cuvant:
    litera_mica = litera.lower()
    if litera_mica in dict1:
        dict1[litera_mica] +=1
    else:
        dict1[litera_mica] = 1

dict = {litera:frecventa for litera, frecventa in dict1.items()}
print(dict)