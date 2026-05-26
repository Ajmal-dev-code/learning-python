def grade(number):
    if number >= 90:
        return "o"
    elif number >= 75:
        return "A"
    elif number >= 60:
        return "B"
    elif number >= 50:
        return "c"
    elif number >= 33:
        return "D"
    else:
        return "fail"

def average(maths, science, sst, english, hindi, vac):
    return (maths + science + sst + english + hindi + vac)/6
def status(average, maths, science, sst , english , hindi):
    if average >= 33:
        if maths >= 33 and science >= 33 and sst >=33 and english >= 33 and hindi >= 33:
            return "Pass"
        elif maths <= 33 and science >= 33 and sst >=33 and english >= 33 and hindi >= 33:
            return "pass"
        elif maths >= 33 and science <= 33 and sst >=33 and english >= 33 and hindi >= 33:
            return "pass"
        elif maths >= 33 and science >= 33 and sst <=33 and english >= 33 and hindi >= 33:
            return "pass"
        elif maths >= 33 and science >= 33 and sst >=33 and english <= 33 and hindi >= 33:
            return "pass"
        elif maths >= 33 and science >= 33 and sst >=33 and english >= 33 and hindi <= 33:
            return "pass"
        else:
            return "fail"
    else:
        return "fail"
    
def display_result(name, class_and_section, maths, science, sst, english, hindi, vac):
    total = maths + science + sst + english + hindi + vac
    average = total/6

    print(f'''         -----*{name} REsult*-----
              class and section = {class_and_section}
          maths number is      {maths}   Grade {grade(maths)}
          science number is    {science}   Grade {grade(science)} 
          sst number is        {sst}   Grade {grade(sst)}
          english number is    {english}   Grade {grade(english)}
          hindi number is      {hindi}   Grade {grade(hindi)}
          vac number is        {vac}   Grade {grade(vac)}
          Total number is      {total}
          you percentage is {average:.2f}
          you got {grade(average)} Grade
          your are {status(average, maths, science, sst, english, hindi)}''')

name = input("Enter your name: ")
class_and_section = input("Enter your class and Section: ")
maths = int(input("Enter your maths no: "))
science = int(input("Enter your science no: "))
sst = int(input("Enter your sst no: "))
english = int(input("Enter your english no: "))
hindi = int(input("Enter your hindi no: "))
vac = int(input("Enter your vac no: "))

display_result(name, class_and_section, maths, science, sst, english, hindi, vac)