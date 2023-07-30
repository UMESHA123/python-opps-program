keys = [1,2,3,4]
values = ['umesha','ramesha','hugger']

l = dict(zip(keys,values))
print(l)

#above the program is to convert the two list into dict

#the below the program is convert the dict to tupple

for item in l.items():
    print(item)
    
#combine this two steps for list to tupple converstion

# The below the program is for accessing the tupple value
for k,v in l.items():
    print(k,' ',v)
