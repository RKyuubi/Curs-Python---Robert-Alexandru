math_grades = {'Marius': 8.0,'Andreea': 9.5,'Adrian': 7.9,'Bianca': 10}
nota_maxima = max(math_grades.values())

for elev, nota in math_grades.items():
    if nota == nota_maxima:
        print(f"{elev} cu nota {nota}")