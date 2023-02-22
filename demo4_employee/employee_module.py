class Employee:
    company_name = None # static variable or class variable
    company_location = None

    def __init__(self):
        self.emp_id = None # non static variable or Instance Variable
        self.emp_name = None
        self.emp_salary = None
        self.emp_performance = None

    @staticmethod
    def print_author_name():
        print("Author Name"," Balaji Dinakar")

    def display_employee_record(self):
        print(35*"-")
        print("Employee Id :", self.emp_id)
        print("Employee Name :", self.emp_name)
        print("Employee salary:", self.emp_salary)
        print("Employee Performance", self.emp_performance)
        print("Employee Company ",Employee.company_name)
        print("Employee Location", Employee.company_location)
        print("-" * 35)

    def calculate_bonus(self):
        if self.emp_performance == "A":
            print("40% Bonus")
            self.emp_salary =self.emp_salary + (self.emp_salary*40)/100
        elif self.emp_performance == "B":
            print("30% Bonus")
            self.emp_salary = self.emp_salary+(self.emp_salary * 30) / 100
            print(self.emp_salary)
        elif self.emp_performance == "C":
            print("20% Bonus")
            self.emp_salary = self.emp_salary + (self.emp_salary * 20) / 100
        else:
            print("NO Bonus")








