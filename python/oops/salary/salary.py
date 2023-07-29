class Employee:
    def __init__(self,emp_id,emp_name,emp_role,emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_role = emp_role
        self.emp_salary = emp_salary
    
    def increment_salary(self,number):
        result = (self.emp_salary + self.emp_salary*(number/100))
        return result
    
class Organization:
    def __init__(self,employee_obj):
        self.employee_obj = employee_obj
    def calculate_salary(self,string,number):
        result = {}
        for obj in employee_obj:
            if string == obj.emp_role:
                r = Employee.increment_salary(obj,number)
                result[obj.emp_name] = r
        return result

n = int(input())
employee_obj = []
for i in range(n):
    emp_id = int(input())
    emp_name = input()
    emp_role = input()
    emp_salary = int(input())

    employee_obj.append(Employee(emp_id,emp_name,emp_role,emp_salary))

obj = Organization(employee_obj)

string = input()
number = int(input())
result = obj.calculate_salary(string,number)
print(result)
