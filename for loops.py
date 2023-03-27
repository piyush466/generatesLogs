# list = [["piyush",1],["good",2],["morning",3],["afternoon",4]]
#
# dict =dict(list)
# for l in dict:
#     print(l)

# list = [["piyush",1],["good",2],["morning",3],["afternoon",4]]
#
# for iterm,numbers in list:
#     print(iterm,"item and number is",numbers)

list = [int,float,"piyush",23,34,234,54,7,6,7434,3,32,32,1,3,4,57,76,5,]
print(type(list))
for i in list:
    if str(i).isnumeric() and i >6 :
        print(i)