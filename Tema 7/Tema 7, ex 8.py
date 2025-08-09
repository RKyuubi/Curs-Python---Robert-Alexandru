cars = {
    'Dacia': 15000,
    'Toyota': 20000,
    'BMW': 50000,
    'Audi': 45000,
    'Hyundai': 16500,
    'Mercedes': 70000
}

dictionar_masini_mai_ieftine ={}

for nume,pret in cars.items():
    if cars[nume] < 40000:
        dictionar_masini_mai_ieftine[nume] = pret

print(f"\nMasini mai ieftine de 40.000 de euro \n{dictionar_masini_mai_ieftine}")

dictionar_preturi_lei ={}

for nume,pret in cars.items():
    dictionar_preturi_lei[nume] = pret *5

print(f"\nPretul masinilor in RON \n{dictionar_preturi_lei}")