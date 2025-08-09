numar = 10

numar_introdus = int(input("introduceti numarul:"))
while numar_introdus != numar:
    if numar_introdus < numar:
        print (f"Introdu un numar mai mare")
        numar_introdus = int(input("Introduceti alt numar:"))
    elif numar_introdus > numar:
        print (f"Introdu un numar mai mic")
        numar_introdus = int(input("Introduceti alt numar:"))


print (f"Felicitari ai ghicit numarul")
