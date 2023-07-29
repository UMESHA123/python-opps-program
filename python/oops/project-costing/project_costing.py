class Project:
    def __init__(self,project_id,project_name,man_hours,technology_list):
        self.project_id = project_id
        self.project_name = project_name
        self.man_hours = man_hours
        self.technology_list = technology_list
        self.avg_project_cost = 0
        
    def calculateProjectCost(self,rate_per_man_hours):
        project_cost = self.man_hours * rate_per_man_hours
        return project_cost

class Organisation:
    def __init__(self,obj_list):
        self.obj_list = obj_list
    
    def projectAvgVostByTechnology(self,find_id,rate_per_man_hours):
        is_match = False
        for obj in self.obj_list:
            if find_id == obj.project_id:
                is_match = True
                project_cost = Project.calculateProjectCost(obj,rate_per_man_hours)
                obj.avg_project_cost = project_cost/len(obj.technology_list)
            
                print(len(obj.technology_list),' ',obj.avg_project_cost)
                
            
                return [[obj.project_id,obj.project_name,obj.technology_list]]
            
        if not is_match:
            return None
        


n = int(input())
obj_list = []

for i in range(n):
    technology_list = []
    project_id = int(input())
    project_name = input()
    man_hours = int(input())
    
    for j in range(int(input())):
        technology_list.append(input())
    obj_list.append(Project(project_id,project_name,man_hours,technology_list))


obj = Organisation(obj_list)

find_id = int(input())
rate_per_man_hours = int(input())

result = obj.projectAvgVostByTechnology(find_id,rate_per_man_hours)

if result == None:
    print('No project Exits!')
else:
    for item in result:
        print(item,end=' ')


