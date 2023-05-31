# Initialize an empty list to store student information
students = []

# Read the number of students
num_students = int(input("Enter the number of students: "))

# Read the name and grade of each student and store them in the list
for _ in range(num_students):
    name = input("Enter the student's name: ")
    grade = float(input("Enter the student's grade: "))
    students.append([name, grade])

# Find the second lowest grade
grades = set()
for _, grade in students:
    grades.add(grade)
second_lowest_grade = sorted(grades)[1]

# Find the names of the students with the second lowest grade
names = []
for name, grade in students:
    if grade == second_lowest_grade:
        names.append(name)

# Sort the names alphabetically
names.sort()

# Print each name on a new line
for name in names:
    print(name)