def nameTo(string):
    return f"My qualification is {string}"

def add(a,b):
    return a+b+10

print("test ",__name__)
if __name__ == '__main__':
    print(nameTo("MCA"))
    pi = add(2,5)
    print(pi)