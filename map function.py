number = ["2","4","7","5","9"]

# number = list(map(int,number))
#
# def add(number):
#     return number*2
#
# a = add(number)
# print(a)
#
# def sq(a):
#     return a*a
# num =[2,4,3,34,5,6]
# sqaure = list(map(sq,num))
# print(sqaure)

def square(a):
    return a*a

def cube(b):
    return b*b*b
func = [square,cube]
print("Square","Cubes")
for i in range(5):
    # val = list(map(lambda x:x(i),func))
    val =[square(i),cube(i)]
    print(val)



