employees = ['Michal', 'Harry', 'Susan', 'Dan', 'Christen']
email = ['michal@comp.com', 'harryf@comp.com',
         'susan@comp.com', 'dan2@comp.com', 'chris@comp.com']
dict1= {}

for i in range (len(employees)):
    employees_name = employees[i]
    employees_email = email[i]
    dict1[employees_name] = employees_email

print (dict1,"\n")

for employee, email in dict1.items():
    print (f"{employee} - {email}")