# Employee Organisation

# 2
# A
# 1
# 30
# M
# B
# 2
# 40
# F
# 10
# 50

class Employee1:
    def __init__(self,name,id,age,gender):
        self.name = name
        self.id = id
        self.age = age
        self.gender = gender

class Organisation:
    def __init__(self,obj_list):
        self.obj_list = obj_list
    
    def find_employee_age(self,find_id):
        for obj in self.obj_list:
            if obj.id == find_id:
                return obj.age
            else:
                return -1
    #this method counts the total number of employee
    def get_employee_count(self):
        return len(self.obj_list)
    
    #this method is count the number of employee based on the id
    def count_employee(self,find_id):
        count = 0
        for obj in self.obj_list:
            if obj.id == find_id:
                count = count + 1
        return count

n = int(input())
obj_list = []
for i in range(n):
    name = input()
    id = int(input())
    age = int(input())
    gender = input()
    obj_list.append(Employee1(name,id,age,gender))

find_id = int(input())
find_age = int(input())

obj = Organisation(obj_list)
result_age=obj.find_employee_age(find_id)
print(result_age)
print(obj.get_employee_count())

print(obj.count_employee(find_id))



