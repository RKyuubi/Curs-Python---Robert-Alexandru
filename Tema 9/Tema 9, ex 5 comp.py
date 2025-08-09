list = [1, 2, 3, 'Python', 'java']

#fara list comprehension
lista_true_false = []

for element in list:
    if isinstance(element, int):
        lista_true_false.append(False)
    else:
        lista_true_false.append(True)

print(lista_true_false)

#cu list comprehension
lista_true_false = [not isinstance(element, int) for element in list]
print(lista_true_false)