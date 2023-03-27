class A:
    def __init__(self,m):
        self.money = m
        print("test 1")


    def show(self):
        print("my name is {}")

class B(A):
    def __init__(self,m,a):
        super().__init__(m)
        self.age =a
        print("test 2")

    def test(self):
        print(f"test name {self.money} age: {self.age}")

s = B(100,2)
s.test()