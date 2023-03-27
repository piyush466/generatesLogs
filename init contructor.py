class Constructor:

    def __init__(self,name,age,se_class):
        self.name = name
        self.age = age
        self.se_class =se_class

    def ptintFunctionRun(self):
        return f"My name is {self.name} and my age is {self.age}, and i study in {self.se_class}th class"


piyush = Constructor("piyush",24,"12")
tushar = Constructor("Tushar",20,"11")
print(tushar.ptintFunctionRun(), piyush.ptintFunctionRun())

# print(t)