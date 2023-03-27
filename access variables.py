class NewVariables:
    var= 10
    _protec = 100     # protect variable user only familys
    __private =2000
    def __init__(self,name,age):
        self.name = name
        self.age =age

    def returnf(self):
        return f"My name is {self.name} and age is {self.age}"


vari = NewVariables("piyush",22)
print(vari.returnf())
print(vari._NewVariables__private)
print(vari._protec)

