secret_number = 5688
print("Welcome to number guessing game: ")
print("-----start-----")
print("only one rule you will get only 5 chance to guess")
for i in range(5):
    number = int(input("Enter your number:  "))
    if number == secret_number:
        print("you got it you won.")
        break
    elif number < secret_number:
        print("number is lower than actuall number")
    elif number > secret_number:
        print("number is higher than actuall number")
else:
    print("Better luck next time")
    
print("I hope you Enjoy the game.")