# class Methodd:
#     leave = 12
#
#     def __init__(self, name, age, se_class):
#         self.name = name
#         self.age = age
#         self.se_class = se_class
#
#     def ptintFunctionRun(self):
#         return f"My name is {self.name} and my age is {self.age}, and i study in {self.se_class}th class"
#
#     @classmethod
#     def classmethodEdit(cls,a):
#         cls.leave = a
#
#
# piyush = Methodd("piyush", 24, "12")
# tushar = Methodd("Tushar", 20, "11")
#
# piyush.classmethodEdit(22)
# print(piyush.leave)



# class NewOne:
#     salary = 10000
#
#     def __init__(self,name,salary1):
#         self.name= name
#         self.salary1 = salary1
#
#     def funcreturn(self):
#         return f"My name is {self.name}, and salary is {self.salary1}"
#
#     @classmethod
#     def change_class(cls,sal):
#         cls.salary = sal
#
# piyush = NewOne("piyush",23333)
# print(piyush.funcreturn())
#
# piyush.change_class(4555)
# print(piyush.salary)
#
# print(NewOne.salary)



class Jack:
    variabl = 230

    def __init__(self, name, salary1):
        self.name = name
        self.salary1 = salary1


    def funcreturn(self):
        return f"My name is {self.name}, and salary is {self.salary1}"

    @classmethod
    def change_variable(cls,var):
        cls.variabl = var

    @classmethod
    def from_dashSplit(cls,str):
        return cls(*str.split("-"))

piyush = Jack("piy",1111)
tushar  =Jack("tushsar",200)

karan = Jack.from_dashSplit("karan-2222")
print(karan.name,karan.salary1)

print(tushar.funcreturn(),"\n",piyush.funcreturn())


print(piyush.variabl)
piyush.change_variable(20000)
print(piyush.variabl)

print(tushar.variabl)























