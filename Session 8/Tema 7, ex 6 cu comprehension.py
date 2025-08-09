info_grades = {
    'Maria': [8, 9, 10],
    'Bogdan': [8.6, 7.3, 9.9, 10],
    'Ilinca': [10, 10],
    'Andra': [9.5, 7, 9],
    'Daniel': [6, 10, 9.7]
}

lista = [Nume for Nume in info_grades if len(info_grades[Nume])==3]
print(lista)

dictionar_medii = {nume: sum(info_grades[nume]) / len(info_grades[nume]) for nume,note in info_grades.items()}
print(dictionar_medii)

media_maxima = max(dictionar_medii.values())
elevi_nota_maxima = [nume for nume, medie in dictionar_medii.items() if medie ==media_maxima]
print(elevi_nota_maxima)