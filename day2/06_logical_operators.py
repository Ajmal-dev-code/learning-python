#and for checking both conditon when both setisfy only then run
age = int(input("Enter you age sir: "))
if age >= 18 and age == 30:
    print("special 30% discount for you wish you luck")

#or only one condtion need to setisfy and it runs
if age >= 18 or age <=30:
    print("you can go park to play")

#not revese the decision true becomes false condtion 
if not age == 18:
    print("you are right")

citizen = True
if age >= 18 and citizen:
    print("your are good to go")