
def add_student():
    with open("student.txt", "a") as file:
        while True:
            try:
               name = input("Enter student name: ")
               if name.lower() == "exit":
                   break
               age = int(input("Enter student age: "))
               grade = float(input("Enter student grade: "))

               file.write(f"Name = {name}, Age = {age}, Grade = {grade}\n")
               print(f"{name} successfully added to the file.")
               print("to quite enter exit.")
               print("program done go and check'student.txt' file for your added data.") 
            except ValueError:
               print("Invalid input")

def read_student_record():
    with open("student.txt", "r") as file:
        details = file.read()
        print(details)

def search_student():
    search_name = input("Enter student name: ")
    found = False
    try:
        with open("student.txt", "r") as file:
            for line in file:
                cleaned_line = line.strip()
                student_data = cleaned_line.split(",")
                if len(student_data) != 3:
                    continue

                name = student_data[0].replace("Name = ", "")
                age = student_data[1].replace(" Age = ", "")
                grade = student_data[2].replace(" Grade = ", "")

                if name.lower() == search_name.lower():
                    print("\n----student found----\n")
                    print(f"Name : {name}\n")
                    print(f"Age : {age}\n")
                    print(f"Grade : {grade}\n")
                    found = True
                    break
        if not found :
            print("Entered student name not present in the file. ")
    except ValueError:
        print("Wrong input sir. sorry for inconvnience")
        
print("Welcom to our system sir/Mam")
while True:
    print('''we offer these services here
      for reading student file write r
      for adding student write add
      for searching student write search
      for exit type exit''')
    try:
       option = input("enter your choice sir/mam: ")
       if option == "r":
           read_student_record()
       elif option == "add":
            add_student()
       elif option == "search":
            search_student()
       elif option == "exit":
            print("Thankyou for using our system.")
            break
       else:
            print("Your input did't match our options sorry sir/mam")

    except ValueError:
        print("Invalid input")
    