from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def area(self):
        return 0

class Rectangle(A):
    tp  = "rect"
    side = 4
    def __init__(self):
        self.lenght =4
        self.breath =7

    # def returnfu(self):
    #     return self.breath * self.lenght

obj = Rectangle()
print(obj)
print(obj.returnfu())