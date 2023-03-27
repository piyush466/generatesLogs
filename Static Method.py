
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

    @staticmethod
    def static_met(str):
        # print("my naem is "+str)
        return "test " +str

piyush = Jack("piy",1111)
tushar  =Jack("tushsar",200)
#
# hi =piyush.static_met("hero")
# print(hi)

a = Jack.static_met("piyush again")
print(a)

