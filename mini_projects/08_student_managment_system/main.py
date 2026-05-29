import student
import storage
 
print("Welcome to Student Management System: ")
while True:
    print('''for adding student write a
for search studnt write s
for update student write u
for reading student details write r
for quit write exit''')
    
    choice = input("Enter your choice: ")
    if choice == "a":
        student.add_student()
    elif choice == "s":
        student.search_student()
    elif choice == "u":
        student.update_student
    elif choice == "r":
        storage.read_student
    elif choice == "exit":
        break
    else:
        print("invalid input sir")

