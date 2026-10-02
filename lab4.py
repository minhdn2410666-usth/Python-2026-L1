def input_student():
    name = input("Name: ")
    courses = input("Courses: ")
    marks = input("Marks: ")
    with open("students.txt", "a") as f:
        f.write(name + "\n")
    with open("courses.txt", "a") as f:
        f.write(courses + "\n")
    with open("marks.txt", "a") as f:
        f.write(marks + "\n")
    return name, list(map(float, marks.split())), list(map(int, courses.split()))
import os
import tarfile
import math
from input import input_student
from output import output
from domains.student import Student
if os.path.exists("students.dat"):
    with tarfile.open("students.dat", "r:gz") as f:
        f.extractall()
students = []
n = int(input("Number of students: "))
for i in range(n):
    name, marks, credits = input_student()
    marks = [math.floor(x * 10) / 10 for x in marks]
    students.append(Student(name, marks, credits))
output(students)
with tarfile.open("students.dat", "w:gz") as f:
    f.add("students.txt")
    f.add("courses.txt")
    f.add("marks.txt")
def output(students):
    students.sort(key=lambda x: x.gpa(), reverse=True)
    for s in students:
        print(s.name, round(s.gpa(), 1))
import numpy as np
class Student:
    def __init__(self, name, marks, credits):
        self.name = name
        self.marks = np.array(marks)
        self.credits = np.array(credits)
    def gpa(self):
        return np.sum(self.marks * self.credits) / np.sum(self.credits)
