class Inherit:
    def __init__(self,name,salary,age):
        self.name= name
        self.salary = salary
        self.age = age

    def retunrfun(self):
        return f"my name is {self.name} and salsary is {self.salary},my age is {self.age}"
    def add(self,a):
        return "addition of two number is=",a+a


piyush = Inherit("piyush",15000,23)
print(piyush.retunrfun())
p= piyush.add(2)
print(p)

class Single_level(Inherit):

    def __init__(self, name, salary, age,languages):
        self.name = name
        self.salary = salary
        self.age = age
        self.languages =languages

    def return_new(self):
        return f"my name is {self.name} and salsary is {self.salary},my age is {self.age} and languages is {self.languages}"

print("***********************************************************")
karan = Single_level("karan",20000,20,["pyhton","cpp"])
print(karan.retunrfun())
print(karan.return_new())
