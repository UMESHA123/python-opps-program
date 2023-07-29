class Employee:
    def __init__(self,emp_no,emp_name,leaves):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.leaves = leaves 

class Company:
    def __init__(self,employee_list):
        self.employee_list = employee_list

    def leaves_avilable(self,e_id,leaves_type,no_days):
        for obj in self.employee_list:
            if obj.emp_no == e_id:
                for k,v in obj.leaves.items():
                    if k == leaves_type:
                        if no_days > v:
                            return 'Rejected'
                        else:
                            return 'Granted'



employee_list = []
for i in range(int(input())):
    emp_no = int(input())
    emp_name = input()
    leaves = {
        'EL':int(input()),
        'CL':int(input()),
        'SL':int(input())
    }
    employee_list.append(Employee(emp_no,emp_name,leaves))

e_id= int(input())
leaves_type = input()
no_days = int(input())

obj = Company(employee_list)
result=obj.leaves_avilable(e_id,leaves_type,no_days)
print(result)








