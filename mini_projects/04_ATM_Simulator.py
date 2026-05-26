correct_username = "Money"
correct_password = "Hungryneedmoney"

balance = 50000
username = input("Enter user name: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Successfully fecthed your details")
else:
    print("Invalid credidentials")
    
print("******Welcom Sir/Mam******")
print('''Features offered in my ATM simulator is:
      1 write CB for checking balance:
      2 write DM for depositing money:
      3 write WM for withdrawing money:
      4 if above 3 opetion are not for you so what the hell are you doing here go away''')
fetures = (input("Enter the feture you wanna use: "))
if fetures == "CB":
    print(f"you balace is {balance}.")
elif fetures == "DM":
    money = int(input("Enter money how much you wanna deposite: "))
    print(f"your balance is {balance + money}")
elif fetures == "WM":
    money = int(input("Enter how much you wanna withdraw: "))
    if money > balance:
        print("Insufficent balance")
    else:
        print(f"your balance is now {balance-money}.")
else:
    print("what are you doing now men just go don't waste my time.")

print("Thankyou for using our ATM simulator i hope you enjoyed.")