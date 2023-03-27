# class First:
#     piyush = 10
#
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age
#
#     def returnn1(self):
#         return f"My name is {self.name}, and age is {self.age}"
#
# class Second:
#
#     piyush = 11
#
#     def __init__(self,name,age,sal):
#         self.name= name
#         self.age= age
#         self.sal = sal
#
#     def reu2(self):
#         return f"my name is {self.name}, and age is {self.age}, and salary is {self.sal}"
#
# class Multiple(Second,First):
#     # piyush = 12
#     lang = "Hindi"
#     def fun(self):
#         print(self.lang)
#
# aryan = Multiple("piyush",24,3300)
# print(aryan.reu2())
#
# print(aryan.piyush)
# print(aryan.piyush)




class First:
    # piyush = 10

    def __init__(self,name,age):
        self.name= name
        self.age= age

    def returnn1(self):
        return f"My name is {self.name}, and age is {self.age}"

class Second:

    # piyush = 11

    def __init__(self,namee,ageg,sal):
        self.name= namee
        self.age= ageg
        self.sal = sal

    def reu2(self):
        return f"my name is {self.name}, and age is {self.age}, and salary is {self.sal}"

class Third(First,  Second):
    pass



shah = Third("piyush",24)
print(shah.returnn1())
























