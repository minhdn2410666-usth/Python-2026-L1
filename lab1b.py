students = []
courses = []
marks = {}

n = int(input("Number of students: "))
for i in range(n):
    students.append(input("Student ID, Name, DoB: "))

n = int(input("Number of courses: "))
for i in range(n):
    courses.append(input("Course ID, Name: "))

for c in courses:
    marks[c] = []
    for s in students:
        marks[c].append(input(f"Mark of {s} for {c}: "))

print("\nStudents:")
print(*students, sep="\n")

print("\nCourses:")
print(*courses, sep="\n")

print("\nMarks:")
print(marks)