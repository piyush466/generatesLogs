class Employee:
    def __init__(self,name,lname):
        self.name= name
        self.lname =lname

    def printall(self):
        return f"my name is {self.name} {self.lname}"

    @property
    def email(self):
        return f"{self.name}.{self.lname}@cliffex.com"

obj = Employee("piyush","Dravyakar")
print(obj.printall())
print(obj.email)

obj.name ="aryan"
print(obj.email)

obj.lname="ghonge"
print(obj.printall())