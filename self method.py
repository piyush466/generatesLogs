class Stud:
    total = 100

    def printClass(self):
        return f"Name is {self.name},and age is {self.age},percentage of grade is {self.grade}"

piyush = Stud()
tushar = Stud()

piyush.name = "piyush"
piyush.age = 20
piyush.grade = "A+"

tushar.name = "tushar"
tushar.age = 24
tushar.grade = "B+"

print(piyush.printClass())
print(tushar.printClass())

