#   ___  _                __   __           _        _     _
#  / __|| | __ _  ___ ___ \ \ / /__ _  _ _ (_) __ _ | |__ | | ___  ___
# | (__ | |/ _` |(_-<(_-<  \ V // _` || '_|| |/ _` || '_ \| |/ -_)(_-<
#  \___||_|\__,_|/__//__/   \_/ \__,_||_|  |_|\__,_||_.__/|_|\___|/__/
#

class Student:

    # Class Variables.
    class_year = 2020
    number_students = 0

    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status
        Student.number_students += 1

student_1 = Student("Julian", 20, "Active")
student_2 = Student("Abid", 18, "Active")
student_3 = Student("Bahlil", 32, "Dead")
student_4 = Student("Lucia", 22, "Active")
student_5 = Student("Samsul", 24, "Inactive")

print(f"Name: {student_1.name}\nAge: {student_1.age}\nStatus: {student_1.status}\nGraduation: {Student.class_year}\n")
print(f"Name: {student_2.name}\nAge: {student_2.age}\nStatus: {student_2.status}\nGraduation: {Student.class_year}\n")
print(f"Name: {student_3.name}\nAge: {student_3.age}\nStatus: {student_3.status}\nGraduation: {Student.class_year}\n")
print(f"Name: {student_4.name}\nAge: {student_4.age}\nStatus: {student_4.status}\nGraduation: {Student.class_year}\n")
print(f"Name: {student_5.name}\nAge: {student_5.age}\nStatus: {student_5.status}\nGraduation: {Student.class_year}\n")

# Good Practice.
print(Student.class_year)
print(Student.number_students)
