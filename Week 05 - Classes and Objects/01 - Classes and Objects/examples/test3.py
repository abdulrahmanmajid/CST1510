class student:
    def __init__(self, name, program, mark):
        self.name = name
        self.program = program
        self.mark = mark

students = []

path = "/Users/abdulrahman/Uni Projects/CST1510/Week 05 - Classes and Objects/01 - Classes and Objects/examples/data.txt"
with open(path, "r") as file:
    for line in file:
        name, program, mark = line.strip().split(",")
        s = student(name, program, int(mark))
        students.append(s)

print("Student Details")
print("----------------")

for student in students:
    print("Name:", student.name)
    print("Program:", student.program)
    print("Mark:", student.mark)
    print("----------------")


print("Total Students:", len(students))