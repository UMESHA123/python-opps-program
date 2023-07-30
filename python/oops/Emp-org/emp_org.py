class Employee:
    def __init__(self,name,id,age,gender):
        self.name = name
        self.id = id
        self.age = age
        self.gender = gender

class Organasation:
    def __init__(self,obj_list):
        self.obj_list = obj_list
    
    def get_employee_count(self):
        count = 0
        for obj in self.obj_list:
            if obj.name:
                count = count + 1
        return count
    
    def find_employee(self,find_id):
        isMatch = False
        for obj in self.obj_list:
            if obj.id == find_id:
                isMatch = True
                return obj.age
        if not isMatch:
            return None

    def countEmployee(self,f_age):
        count = 0
        for obj in self.obj_list:
            if obj.age == f_age:
                count = count + 1
        return count
        
obj_list = []
n = int(input())

for i in range(n):
    name = input()
    id = int(input())
    age = int(input())
    gender = input()
    obj_list.append(Employee(name,id,age,gender))
    
find_id = int(input())
f_age = int(input())

obj = Organasation(obj_list)

count = obj.get_employee_count()
print(count)

result = obj.find_employee(find_id)
if result == None:
    print('not found')
else:
    print(result)
    
r = obj.countEmployee(f_age)
print(r)