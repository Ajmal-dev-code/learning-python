#inside function we use print() to print but it does't store that so the output we can not use in codes again.
#instead we use return to store our output and can use outside the functions

def add( a, b):
    return(a + b)
print(add(4, 8))
#both are diffrent
def addprint(a, b):
    print(a + b)
addprint(4, 8)
