inceput_interval = int(input("Introduceti numarul de inceput al intervalului: "))
sfarsit_interval = int(input("Introduceti numarul de sfarsit al intervalului: "))

lista_pp =[]
if inceput_interval > sfarsit_interval:
    print("Numarul de inceput nu poate fi mai mare decat numarul de sfarsit")
else:
    print (f"\nPatratele perfecte intre {inceput_interval} si {sfarsit_interval} sunt:")
    gasit_patrat_perfect = False
    i = 0
    while True:
        patrat_perfect = i*i
        if patrat_perfect > sfarsit_interval:
            break
        elif patrat_perfect >= inceput_interval:
            lista_pp.append(patrat_perfect)
            gasit_patrat_perfect = True
        i += 1
    if not gasit_patrat_perfect:
        print ("Nu s-au gasit patrate perfecte in intervalul specificat")

print(lista_pp)

# Am facut mai sus fara list comprehension pentru a ma asigura de cum functioneaza patratele perfecte

if inceput_interval > sfarsit_interval:
    print("Numarul de inceput nu poate fi mai mare decat numarul de sfarsit")
else:
    sfarsit_interval_i = int(sfarsit_interval**0.5)+2
    lista_pp2 = [i*i for i in range(sfarsit_interval_i) if inceput_interval <= i*i <= sfarsit_interval]
print(lista_pp2)