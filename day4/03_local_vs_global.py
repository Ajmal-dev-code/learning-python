#local means variable defined under function
#global means variable defined outside the function
#function can not change the value of global value 
#it copys the global value and assign to local variable

x = 10
def test():
    x = 5
    print(x)
print(x)
test()