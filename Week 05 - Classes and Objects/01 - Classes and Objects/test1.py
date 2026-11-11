

class student:

    def __init__(self, name, DOB, program, mark):
        self.name = name
        self.DOB = DOB
        self.program = program
        self.mark = mark

    def grade(self):
        if self.mark >= 40:
            print ("Grade is Pass")
        else:
            print ("Grade is Fail")

    def findAge(self):
        print (self.DOB)

print(student)

std1 = student("ali", "01/01/2000", "BSCS", 50)
std2 = student("ahmed", "01/01/2001", "BSSE", 30)



std1.findAge()
std1.grade()

std2.findAge()
std2.grade()

