class Employee:
    def __init__(self,name,designation,salary,loan_details):
        self.name = name
        self.designation = designation
        self.salary = salary
        self.loan_details = loan_details
        
class Organasation:
    def __init__(self,employee_obj_list,loan_type,amount_want_toborrow):
        self.employee_obj_list = employee_obj_list
        self.loan_type = loan_type
        self.amount_want_toborrow = amount_want_toborrow

        
    def eligible(self,emp_name,loan_type,amount_want):
        for obj in self.employee_obj_list:
            if obj.name.lower() == emp_name:
                if loan_type.lower() not in obj.loan_details:
                    if loan_type.lower() in obj.loan_details:
                        borrow = amount_want
                        for k,v in obj.loan_details.items():
                            borrow = borrow + v
                        
                            
    
n = int(input())
employee_obj = []
for i in range(n):
    name = input()
    designation = input()
    salary = int(input())
    loan_details = {}
    for i in range(int(input())):
        loan_details['type'] = input()
        loan_details['amount'] = int(input())
    
    employee_obj.append(Employee(name,designation,salary,loan_details))

obj = Organasation(employee_obj)

emp_name = input()
loan_type = input()
amount_want = int(input()) 

result = obj.eligible(emp_name,loan_type,amount_want)






