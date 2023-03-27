# b = "piyush"
# c = "test "
# a = f"good test {}"

# tuple = ("python ")*10*2
# print(tuple)
#
# def hgfhg(a,b):
#     return a -b
#
# g= hgfhg(6,4)
# print(g)


# a = "piyush"
# b = "dravyakar"
#
# c= f"my name is {a},and sername is {b}"
# print(c)




def add_messages(func):
    def _add_messages():
        print("first ")
        func()
        print("last")
    return _add_messages()







@add_messages
def greet():
    print("Hello, World!")

greet()















