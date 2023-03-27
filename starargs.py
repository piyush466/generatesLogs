def arguments(*args,**kwargs):
    for item in args:
        print(item)
    print("******************************")
    for key,value in kwargs.items():
        print(f"your keys is {key} and value is {value}")


test =["piyush","test","today"]
arguments(*test)

dict = {"hello":"Bye","developer":"tester","yes":"No"}
arguments(**dict)

