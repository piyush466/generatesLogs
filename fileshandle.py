# f = open("piyush2.txt","a")
# a = f.write("piyush good boy\n")
# print(a)
# f.close()


# r+ read and write mode
# f = open("piyush2.txt","r+")
# print(f.read())
# f.write("i like python\n")
# print(f.read())
# f.close()




piyush  = open("piyush2.txt")
print(piyush.tell())
print(piyush.readline())
# print(piyush.tell())
piyush.seek(0)
print(piyush.readline())
print(piyush.tell())
print(piyush.readline())
print(piyush.tell())
piyush.seek(0)
print(piyush.readline())



















