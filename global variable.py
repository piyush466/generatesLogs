# # global variable a
# a =20
# def function(n):
#     # a= 10
#     l = 40
#     # local variable l
#     global a
#     a= a + 1
#     print(a+l)
#     print(n)
# # function("good")
# function("t")












gl = 10
def func():
    a = 20
    global gl
    gl = 20
    print(a + gl)

func()
print(gl)



















