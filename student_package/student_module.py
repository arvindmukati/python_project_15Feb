class Student:
    school_name = None
    school_address = None

    def __init__(self, studentid =None, studentname = None, studentmailid= None, studentpercentage = None):
        self.studentid = studentid
        self.studentName = studentname
        self.studentMailid = studentmailid
        self.studentPercentage = studentpercentage

    def print_grade(self):
        if self.studentPercentage > 100 or self.studentPercentage < 0:
            print("Invalid input")
        elif self.studentPercentage >= 90:
            print("Grade A")
        elif self.studentPercentage >= 80 and self.studentPercentage <= 89:
            print("Grade B")
        elif self.studentPercentage >= 60 and self.studentPercentage <= 79:
            print("Grade C")
        else:
            print("Failed, Please re-attempt")
    @property
    def get_student_name(self):
        return self.studentName

    def get_name_with_percentage(self):
        return ("Hi",self.studentName , "- Your Percentage is", self.studentPercentage)

    @staticmethod
    def get_school_detail():
        return Student.school_name +"is located at" + Student.school_address

