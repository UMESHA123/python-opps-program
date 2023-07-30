sen = input()
sen = sen.split()
di = {}
for word in sen:
    if word not in di.keys():
        di[word] = 1
    else:
        di[word] += 1
print(di)

#or 
di = {}
for word in sen:
    if word not in di.keys():
        di[word] = 0
    di[word] += 1
print(di)
