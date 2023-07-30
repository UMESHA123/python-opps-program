str1 = 'NAINA'
str2 = 'REENE'
l = []
for letter in str1:
    if letter in str2:
        if letter not in l:
            l.append(letter)

for s in l:
    print(s)
    
#in the above the strings only the N is the comman letter

