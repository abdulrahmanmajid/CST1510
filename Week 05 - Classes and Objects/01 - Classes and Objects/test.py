

class student:
    name = ""
    DOB = ""
    program = ""
    mark = 0

    def grade(self):
        if self.mark >= 40:
            print ("Pass")
        else:
            print ("Fail")

    def getAge(self):
        print (self.DOB)

print(student)

std1 = student()

std1.name = "ali"
std1.DOB = "01/01/2000"
std1.program = "BSCS"
std1.mark = 50

std2 = student()
std2.name = "ahmed"
std2.DOB = "01/01/2001"
std2.program = "BSSE"
std2.mark = 30

std1.findAge()
std1.grade()

std2.findAge()
std2.grade()

