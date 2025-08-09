cars = {
    'Dacia': 15000,
    'Toyota': 20000,
    'BMW': 50000,
    'Audi': 45000,
    'Hyundai': 16500,
    'Mercedes': 70000
}

dictionar_masini_mai_ieftine ={}

dictionar_masini_mai_ieftine = {nume:pret for nume,pret in cars.items() if pret >20000}
print (dictionar_masini_mai_ieftine)

dictionar_preturi_lei ={}

dictionar_preturi_lei = {nume:pret*5 for nume,pret in cars.items()}
print(dictionar_preturi_lei)