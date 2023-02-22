from demo4_employee.employee_module import Employee

print(Employee.company_name)
print(Employee.company_location)

Employee.company_name = "Einfochips"
Employee.company_location = "Ahmedabad"

print(Employee.company_name)
print(Employee.company_location)

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()



emp1.emp_id = 101
emp1.emp_name = "Saul"
emp1.emp_salary = 910000
emp1.emp_performance = "A"

emp2.emp_id = 102
emp2.emp_name = "KIM"
emp2.emp_salary = 900000
emp2.emp_performance = "B"

emp3.emp_id = 103
emp3.emp_name = "paul"
emp3.emp_salary = 920000
emp3.emp_performance = "C"

print(emp1.emp_id)
print(emp1.emp_name)
print(emp1.emp_salary)
print(emp1.emp_performance)

print(emp2.emp_id)
print(emp2.emp_name)
print(emp2.emp_salary)
print(emp2.emp_performance)

print(emp3.emp_id)
print(emp3.emp_name)
print(emp3.emp_salary)
print(emp3.emp_performance)

print(type(emp1))

print(emp1.emp_id)
print(emp2.emp_id)
print(emp3.emp_id)

Employee.print_author_name()
emp1.display_employee_record()
emp2.display_employee_record()
emp3.display_employee_record()

emp1.calculate_bonus()
emp2.calculate_bonus()
emp3.calculate_bonus()
print(emp1.emp_salary)
print(emp2.emp_salary)
print(emp3.emp_salary)



