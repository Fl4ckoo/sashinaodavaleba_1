class Employee:
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    
file_csv = open("dataset1.csv", "r")
employees_list = [i.strip() for i in file_csv]
list1 = []

for i in employees_list:
    if employees_list.index(i) == 0:
        pass
    else:
        employees = Employee(i.split(",")[0], i.split(",")[1], i.split(",")[2], i.split(",")[3])
        list1.append(employees)

salary_minimum = [int(i.salary) for i in list1]
age_maximum = [int(i.age) for i in list1]

for i in list1:
    if min(salary_minimum) == int(i.salary):
        print(f"{i.name} has the lowest salary which is {i.salary}$")

for i in list1:
    if max(age_maximum) == int(i.age):
       print(f"{i.name} is the oldest person with {i.age} age")

