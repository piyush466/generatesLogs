# class Dad:
#     basket = 1
#
# class Son(Dad):
#     dance = 1
#     def is_dance(self):
#         return f"yes i dance {self.dance}"
#
# class grandSon(Son):
#     dance = 6
#
#     def is_dance(self):
#         return f"yes i dance grandson {self.dance}"
#
# darry = Dad()
# larry =Son()
# harry =grandSon()
#
# print(harry.is_dance())
# print(harry.basket)
#
# print(darry.basket)





class One:
    bottle = 100

class Two(One):
    cat =12

    def IhaveCat(self):
        return f"i have to much cats {self.cat}"

class Three(Two):
    hello= 20
    cat =20

    def IhaveCat(self):
        return f"i have to much cats {self.cat}"

On = One()
tw = Two()
Thr = Three()

print(Thr.IhaveCat())
print(Thr.bottle)




















