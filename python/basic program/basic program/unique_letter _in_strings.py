str1 = 'NAINA'
str2 = 'REENE'

str1 = list(set(str1))
str2 = list(set(str2))

print(str1)#uniqu letter in str1
print(str2)#uniqu ltter in str2

#form this also we can get the command letter in both the string
#for example
for letter in str1:
    if letter in str2:
    
        print(letter)



#output    
#['I', 'N', 'A']
#['R', 'N', 'E']
#N
# 
# 

#this operation such as & | ^ or only for set() bilt in functio
#if we use this with the list it will gives an error
# #comapering two string with & operater
str1 = 'NAINA'
str2 = 'REENE'

str1 = set(str1)
str2 = set(str2)

lst = str1 & str2
print(lst)

#output is
#{'N'}

lst = str1 ^ str2
print(lst)
# this will print the not command letters
#output is 
#{'I', 'A', 'R', 'E'}

lst = str1 | str2
print(lst)

#uniqu letter in both the string
#output is:
#{'I', 'N', 'R', 'A', 'E'}