class A:
    def __init__(self,name):
        self.name = name

    def test(self):
        return f"my name is {self.name}"

    def __add__(self, other):
        return self.name + other.name


pi = A(20)
sha = A(10)
qa = A(10)
print(pi.test())
print(pi+sha)