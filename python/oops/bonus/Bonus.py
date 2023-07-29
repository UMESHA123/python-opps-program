class Employees:
    def __init__(self,employee_name,designation,salary,overTimeContribution):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = False
   
class Organization:
    def __init__(self,employee_list):
        self.employee_list = employee_list
    
    def check_eligible(self,overTimeThreshould):
        
        for object in self.employee_list:
            totalOverTimeHours = 0
            for k,v in object.overTimeContribution.items():
                totalOverTimeHours += v
                if totalOverTimeHours >overTimeThreshould:
                    object.overTimeStatus = True
    def total_Bonus_Amount(self,rate_per_hours):
        total_bonus = 0
        for object in self.employee_list:
            if object.overTimeStatus:
                for k,v in object.overTimeContribution.items():
                    total_bonus = total_bonus + v * rate_per_hours
            print(object.employee_name," ",object.overTimeStatus)
        return total_bonus

n = int(input())
employee_list = []
for i in range(n):
    employee_name = input()
    designation = input()
    salary = float(input())
    overTimeContribution = {} #name(mount) : overtime(hours)
    #mounth : overtime
    for _ in range(int(input())):
        key = input()
        value = int(input())
        overTimeContribution[key] = value
    employee_list.append(Employees(employee_name,designation,salary,overTimeContribution))
obj = Organization(employee_list)

overTimeThreshould = int(input())

obj.check_eligible(overTimeThreshould)

rate_per_hours = int(input())
result=obj.total_Bonus_Amount(rate_per_hours)

print(result)
