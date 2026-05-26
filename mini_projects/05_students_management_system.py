students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    cgpa = float(input("Enter student CGPA: "))

    student = {
        "Name":name,
        "Age":age,
        "CGPA":cgpa
    }
    students.append(student)
    print("student added successfully")

def display_student():
    if len(students) == 0:
        print("no students found")
        return
    for student in students:
        print(f"Name : {student['Name']}")
        print(f"Age : {student['Age']}")
        print(f"CGPA : {student['CGPA']}")

def search_student():
    search_name = input("Enter name of student: ")
    for student in students:
        if student['Name'].lower() == search_name.lower():
             print("student found")
             print(f"Name : {student['Name']}")    
             print(f"Age : {student['Age']}")    
             print(f"CGPA : {student['CGPA']}")
             return    
    print("Student details not found")

def update_cgpa():
    search_name = input("Enter student name to update it's CGPA: ")
    for student in students:
        if student["Name"].lower() == search_name.lower():
            new_CGPA = float(input("Enter new CGPA: "))
            student["CGPA"] = new_CGPA
            print("CGPA updated successfully")
            return
    print("Student details not found")

while True:
    print('''Welcome to students management system
          for adding student enter add.
          for displaying student enter display
          for searching student enter search
          for updating CGPA Enter update
          for exit enter exit''')
    
    choice = input("Enter your Feature name: ")
    if choice == "add":
        add_student()
    elif choice == "search":
        search_student()
    elif choice == "display":
        display_student()
    elif choice == "update":
        update_cgpa()
    elif choice =="exit":
        print("Thankyou for using our system")
        break
    else:
        print("wrong input sir.")
