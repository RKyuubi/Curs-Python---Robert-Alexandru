lista_numere = [50, 9, 100, 3, 33, '22']

lista2 = [str(numar) if isinstance(numar, int) else numar for numar in lista_numere]

print(f"Lista transformată: {lista2}")