string = input("Enter the string:")
r_string = input("Enter the repeted string:")
count = 0
for index in range(6):
    i = index
    if(string[i] == r_string[0] and string[i+1] == r_string[1] and string[i+2] == r_string[2]):
        count = count + 1
    
print(count)

output
2
