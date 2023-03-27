# def piyush(test):
#     def again():
#         print("one")
#         test()
#         print("three")
#     return again()
#
# @piyush
# def hello():
#     print("two")
#
# # hello = piyush(hello)
# hello()


# def function():
#     print("piyush")
#
# pi = function
# pi()

#
# def exicute(fun):
#     fun("this is")
#
# exicute(print)




# def function1(func):
#     def again():
#         print("one")
#         func()
#         print("three")
#     return again()
#
# @function1
# def piyush():
#     print("two")
#
# piyush()
#
# # p = function1(piyush)
# # p()
#



# Decorator in pythons

def function(test):
    def second_Func():
        print("piyush")
        test()
        print("dravyakar")
    return second_Func()

@function
def Mi():
    print("Milind")



















