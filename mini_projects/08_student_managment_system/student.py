def add_student():
    with open("student.txt", "a") as file:
        while True:
            try:
                name = input("Enter student name: ")
                if name.lower() == "exit":
                    break
                age = int(input("Enter student age: "))
                grade = input("Enter student grade: ")

                file.write(f"Name = {name} , Age = {age} , Grade = {grade}\n")
                print(f"{name} student added succefully to record go and check file.")
                print("to quit wtie exit")
            except ValueError:
                print("Invalid input")

def search_student():
    search_name = input("Enter student name to search: ")
    found = False
    try:
        with open("student.txt", "r") as file:
            for line in file:
                clean_line = line.strip()
                student_data = clean_line.split(",")
                if len(student_data) != 3:
                    continue

                name = student_data[0].replace("Name = ", "")
                age = student_data[1].replace("Age = ", "")
                grade = student_data[2].replace("Grade = ", "")

                if name.lower() == search_name.lower():
                    print("Student details found successfully")
                    print(f"name = {name}\n")
                    print(f"Age = {age}")
                    print(f"Grade = {grade}")
                    found = True
                    break
        if not found:
            print("Student details not found")
    except NameError:
        print("wrong input sir")

def update_student():
    update_name = input("Enter student name to update: ")
    found = False
    try:
        with open("student.txt", "r") as file:
            lines = file.readlines()
        with open("student.txt", "w") as file:
            for line in lines:
                clean_line = line.strip()
                student_data = clean_line.split(",")
                if len(student_data) != 3:
                    continue

                name = student_data[0].replace("Name = ", "")
                age = student_data[1].replace("Age = ", "")
                grade = student_data[2].replace("Grade = ", "")
                if update_name.lower() == name.lower():
                    new_name =  input("Enter new name: ")
                    new_age = int(input("Enter new age: "))
                    new_grade = input("Enter new grade: ")
                    file.write(f"Name = {new_name} , Age = {new_age} , Grade = {new_grade}\n")
                    print("student details upadeted successfully.")
                    found = True
                else:
                    file.write(line)
        if not found:
            print("Student not found")
    except NameError:
        print("Invalid name")
    except FileNotFoundError:
        print("student.txt file not found")
    except ValueError:
        print("invalid age")


