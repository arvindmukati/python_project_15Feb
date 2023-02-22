from student_package.student_module import Student

Student.school_name = ""
Student.school_address = ""
std1 = Student(1001,"jack","jack@gmail.com",45.2)
std2 = Student(studentid=1002,studentname="Peter", studentmailid="peter@gamil.com",studentpercentage=50)
std3 = Student(1002,)
std4 = Student()
std5 = Student()
print(std1.get_student_name)
print(Student.get_school_detail())
