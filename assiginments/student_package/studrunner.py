from Student import student
student.schoolName= "Global School"
student.schoolAddress = "Chennai"

std1 = student()
std2 = student()
std3 = student()

std1.studentRollno = 1001
std1.studentName = "jack"
std1.studentMailid = "jack@gmail.com"
std1.studentPercentage= 45.2


std2.studentRollno = 1002
std2.studentName = "peter"
std2.studentMailid = "peter@gmail.com"
std2.studentPercentage = 85.2


std3.studentRollno = 1003
std3.studentName = "mark"
std3.studentMailid = "mark@gmail.com"
std3.studentPercentage= 56.5
std1.printdata()
std2.printdata()
std3.printdata()
std2.studentMailid = std1.studentMailid
std1.printdata()
std2.printdata()
std3.printdata()

