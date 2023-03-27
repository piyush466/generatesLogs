class Poly:

    def father(self):
        print("i am father")


class Poly2(Poly):

    def mother(self):
        print("i am mother")


class Child(Poly2,Poly):

    def chi(self):
        print("I am child")


fa = Poly()
mo = Poly2()
Ch = Child()
Ch.chi()



