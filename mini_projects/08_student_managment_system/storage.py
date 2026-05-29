def read_student():
    try:
        with open("student.txt", "r") as file:
         return file.readlines()
    except FileNotFoundError:
         return[]
      
def save_student(lines):
   with open("student.txt", "w") as file:
      file.writelines(lines)

