class Employee:
    leaves = 10
    pass

piyush = Employee()
tushar = Employee()

piyush.name = "Piyush"
piyush.age  = 24

tushar.name = "Tushar"
tushar.age = "20"

print("leaves =",tushar.leaves,"name =",tushar.name,"age = ",tushar.age)
piyush.leaves = 12
print(Employee.leaves)
print(piyush.leaves)
print(Employee.__dict__)
print(tushar.__dict__)
