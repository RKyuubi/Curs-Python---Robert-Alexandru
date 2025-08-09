weight = float(input("Introduceti greutatea (in kg):"))
height = float(input("Introduceti inaltimea (in metri):"))

bmi=weight/(height ** 2) #bmi=indicele de masa corporala

print(f"\nIndicele de masă corporală (BMI) este: {bmi:.2f}")

if bmi < 18.5:
    status = "Underweight"
elif bmi >= 18.5 and bmi <= 24.9:
    status = "Healthy weight"
elif bmi >= 25 and bmi <= 30:
    status = "Overweight"
elif bmi >= 30:
    status = "Obesity"

print(f"Status: {status}")