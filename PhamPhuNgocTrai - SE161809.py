"""
Write a student management program in Python. 
Each student object has the following information: 
id, name, gender, age, math grade, physics grade, chemistry grade, grade point average (GPA).
GPA= (math grade+ physics grade + chemistry grade)/3.
The program displays the menu as follows:
o	Add a student to students list
o	Print information about students with the highest GPA
o	Print the list of students in descending order of GPA
o	Remove student based on user id input
o	Save list of student to file
o	Exit

Verify constrain of following data type fields
o	Student ID: max length is 6, not contains special characters (SE0001)
o	Full name: max length is 50
o	Gender: male or female
o	Age: must be a number in range 8 to 50
o	Grade: must be a number in range 0 to 10
"""

import os
import re

def checkID(id):
    if len(id) > 6: 
        print("Max length of student's id is 6!")
        return False
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (regex.search(id) == None):
        return True
    else: 
        print("ID must not contain special character!")
        return False

def checkname(name):
    if len(name) > 50: 
        print("Max length of name is 50 characters!")
        return False
    return True

def checkgender(gender):
    if gender == "male": return True
    if gender == "female": return True
    print("Gender is male or female. ")
    return False

def checkAge(age):
    if 8 <= int(age) <= 50: return True
    print("Age must between 8 and 50!")
    return False

def checkgrade(grade):
    if 0 <= float(grade) <= 10: return True
    print("Grade must between 0 and 10!")
    return False


class Student:
    id = ""
    name = ""
    gender = ""
    age = 0
    math = 0.0
    physics = 0.0
    chemistry = 0.0
    gpa = 0.0

    def __init__(self, id, name, gender, age, math, physics, chemistry):
        self.id = str(id)
        self.name = str(name)
        self.gender = str(gender)
        self.age = int(age)
        self.math = float(math)
        self. physics = float(physics)
        self.chemistry = float(chemistry)
        self.gpa = float((self.math + self.chemistry + self.physics) / 3)

    def set_name(self, newname):
        self.name = newname
    def get_name(self):
        return self.name
    def set_gender(self, newgender):
        self.gender = newgender
    def get_gender(self):
        return self.gender
    def set_age(self, newage):
        self.age = newage
    def get_age(self):
        return self.age
    def set_math(self, newmath):
        self.math = newmath
    def get_math(self):
        return self.math
    def set_physics(self, newphysics):
        self.physics = newphysics
    def get_physics(self):
        return self.physics
    def set_chemistry(self, newchemistry):
        self.chemistry = newchemistry
    def get_chemistry(self):
        return self.chemistry

    def printInfo(self): 
        print("===STUDENT'S INFOMATION===")
        print("ID: ", self.id)
        print("Name: ", self.name)
        print("Gender: ", self.gender)
        print("age: ", self.age)
        print("Math grade: ", self.math)
        print("Physics grade: ", self.physics)
        print("Chemistry grade: ", self.chemistry)
        print("GPA: ", self.gpa)
        print("==========================\n")
    
    def __lt__(self, other):
        return self.gpa > other.gpa
StudentList = list()


def CreateMenu():
    print("""
    - STUDENT MANAGER APPLICATION -
o	0. Clear screen
o	1. Add a student to students list
o	2. Print information about students with the highest GPA
o	3. Print the list of students in descending order of GPA
o	4. Remove student based on user id input
o	5. Save list of student to file
o	6. Exit 
    """) 

def AddStudent(): 
    while True:
        id = str(input("Enter student's id: "))
        if checkID(id): break
    while True:
        name = str(input("Enter student's name: "))
        if checkname(name): break
    while True:
        gender = str(input("Enter student's gender (male / female): "))
        gender = gender.lower()
        if checkgender(gender): break
    while True:
        age = int(input("Enter student's age: "))
        if checkAge(age): break
    while True:
        try:
            math = float(input("Enter student's math grade: "))
            if checkgrade(math): break
        except:
            print("INPUT ERROR!")
    while True:
        try:
            physics= float(input("Enter student's physics grade: "))
            if checkgrade(physics): break
        except:
            print("INPUT ERROR!")
    while True:
        try:
            chemistry = float(input("Enter student's chemistry grade: "))
            if checkgrade(chemistry): break
        except:
            print("INPUT ERROR!")
    StudentList.append(Student(id, name, gender, age, math, physics, chemistry))
    print("STUDENT ADDED SUCCESSFULLY")

def foundStudent(id): 
    for student in StudentList:
        if student.id == id: return True
    print("STUDENT NOT FOUND")
    return False

def HighestGPA(): 
    SortedStudentList = sorted(StudentList)
    index = 0
    print("\nSTUDENT HAS HIGHEST GPA\n")
    SortedStudentList[0].printInfo()
    while SortedStudentList[index].gpa == SortedStudentList[index+1].gpa:
        SortedStudentList[index+1].printInfo()
        index += 1

def PrintDescending(): 
    SortedStudentList = sorted(StudentList)
    for student in SortedStudentList:
        student.printInfo()

def RemoveStudent(): 
    while True:
        keyID = str(input("Enter student's ID: "))
        if checkID(keyID): break
    keydelete = 0
    for index in range(len(StudentList)):
        if StudentList[index].id == keyID:
            keydelete = index
    del StudentList[keydelete]
    print("STUDENT DELETED SUCCESSFULLY")

def SaveToFile(): 
    filename = str(input("Enter file name: "))
    file = open(filename, "w")
    file.write("Student data\n")
    for student in StudentList:
        file.write(student.id +" " + student.name +" "+ student.gender +" "+ str(student.age) +" "+ str(student.math) +" "+ str(student.physics) +" "+ str(student.chemistry) +" "+ str(student.gpa))
        file.write("\n")
    file.close()


def main():
    while True:
        CreateMenu()
        try:
            option = str(input("Enter your option (0 - 6): "))
            if option == '0':
                os.system('cls')
            elif option == '1':
                AddStudent()
            elif option == '2':
                HighestGPA()
            elif option == '3':
                PrintDescending()
            elif option == '4':
                RemoveStudent()
            elif option == '5':
                SaveToFile()
            elif option == '6':
                break
        except: 
            print("INPUT ERROR")
    
def sampledata():
    StudentList.append(Student("se01", "Nguyen Van Bao", "male", 18, 9, 4, 6))
    StudentList.append(Student("se02", "Le Thu Trang", "female", 18, 10, 8, 9)) 
    StudentList.append(Student("se03", "Tran Binh Phuong", "male", 19, 10, 9, 8))
    StudentList.append(Student("se04", "Ly Nha Ky", "female", 19, 3, 4, 2))
    StudentList.append(Student("se05", "Pham Thanh Tung", "male", 18, 8, 6, 7))
    main()

##sampledata()
main()