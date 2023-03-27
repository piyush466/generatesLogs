# class Inherit2:
#     def __init__(self,name,salary,age):
#         self.name= name
#         self.salary = salary
#         self.age = age
#
#     def retunrfun(self):
#         return f"my name is {self.name} and salsary is {self.salary},my age is {self.age}"
#     def add1(self,a):
#         return f"addition of two number is={a+a}"
#
# pi = Inherit2("piyush",3333,22)
# print(pi.retunrfun())
#
# pr = pi.add1(3)
# print(pr)
#
# class Again(Inherit2):
#     def __init__(self, name, salary, age,languages):
#         self.name = name
#         self.salary = salary
#         self.age = age
#         self.languages = languages
#
#     def returncall(self):
#         return f"my name is {self.name} and salsary is {self.salary},my age is {self.age},and languages is {self.languages}"
#
#
# karan = Again("karan",10000,20,["py","cpp"])
# print(karan.returncall())
# tushar = Again("tushar",2332,23,"hhindi")
# print(tushar.returncall())
#
# print(karan.add1(10))
















class Developes:

    def __init__(self,name,age,salary):
        self.name= name
        self.age= age
        self.salary= salary

    def returnfun(self):
        return f"My name is {self.name},and my age is {self.age} my salary is {self.salary}"


piyush = Developes("Piyush",24,15000)
print(piyush.returnfun())


class Testers(Developes):

    def __init__(self,name,age,salary,grade):
        self.name=name
        self.age = age
        self.salary =salary
        self.grade= grade

    def return2(self):
        return f"My name is {self.name},and age is {self.age},my salary is {self.salary}, and grade is {self.grade}"


karna = Testers("karna",24,200000,"A")
print(karna.return2())



































