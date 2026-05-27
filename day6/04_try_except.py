#system crashes if user enter different types of input
number = int(input("Enter a number: "))
#if user enter hello it shows error
# use this
try:#this codes run if input is same as the cosiderable
    number = int(input("Enter number: "))
    print(number)
except ValueError:#other input consider in this
    print("Invalid input")
