numbers = [1, 2, 3, 100, 200, 300]
dict = {}
#fara dict comprehension
for number in numbers:
    if number >= 100:
        dict[number] =True
    else:
        dict[number] = False

print(dict)

#cu dict comprehension
dict2 = {number:(number>=100) for number in numbers}
print(dict2)