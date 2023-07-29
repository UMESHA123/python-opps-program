class Grade:
    def __init__(self,id,name,count_sub,list_sub):
        self.id = id
        self.name = name
        self.count_sub = count_sub
        self.list_sub = list_sub
        
    def claculateGrade(self):
        p = int((sum(self.list_sub))/self.count_sub)
        if p > 80 and p<=100:
            return [p,'A']
        elif p <80 and p>70:
            return [p,'B']
        else:
            return [p,'C'] 

id = int(input())
name = input()
count_sub = int(input())
list_sub = []
for _ in range(count_sub):
    list_sub.append(int(input()))

obj = Grade(id,name,count_sub,list_sub)

g = obj.claculateGrade()
for item in g:
    print(item)