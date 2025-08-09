info_grades = {
    'Maria': [8, 9, 10],
    'Bogdan': [8.6, 7.3, 9.9, 10],
    'Ilinca': [10, 10],
    'Andra': [9.5, 7, 9],
    'Daniel': [6, 10, 9.7]
}

tuplu = ()
# elevi_minimi_3note = 0
for nume, note in info_grades.items():
    if len(note) > 2:
        # elevi_minimi_3note += 1 (acest contor doar imi verifica numarul de elevi cu peste 3 note)
        tuplu += (nume, note)

print(f"Elevii care au cel putin 3 note: {tuplu}")

dictionar_medii = {}
media_note = 0

for nume, note in info_grades.items():
    media_note = sum(note)/len(note)
    dictionar_medii[nume] = media_note

print(f"\nDictionarul nou cu elevii si mediile lor: {dictionar_medii}")

medie_maxima = max(dictionar_medii.values())
elevi_medie_maxima = [] #am creat o lista deoarece pot fi mai multi elevi cu aceeasi medie

for elev, medie in dictionar_medii.items():
    if medie == medie_maxima:
        elevi_medie_maxima.append(elev)

if len(elevi_medie_maxima) == 1:
    print(f"\nElevul/Eleva cu cea mai mare medie este: {elevi_medie_maxima[0]}")
else:
    print(f"\nElevii cu cea mai mare medie sunt: {", ".join(elevi_medie_maxima)}")
