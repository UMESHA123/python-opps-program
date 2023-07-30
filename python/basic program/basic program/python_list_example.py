


def solve():
    list_1 = []
    num = int(input("Enter THE NUMBER:"))
    
    for count in range(num):
        o = input()
        if(o[0::6] == "insert"):
            insert_index = int(o[7])
            insert_value = int(o[9::])
            list_1.insert(insert_index,insert_value)
        elif(o[0::6] == 'remove'):
            remove_value = int(o[8::])
            list_1.remove(remove_value)
        elif(o[0::6] == "append"):
            append_value = int(o[8::])
            list_1.append(append_value)
        elif(o[0::4] == "sort"):
            list_1.sort()
        elif(o[0::4] == "pop"):
            list_1.pop()
        elif(o[0::7] == "reverse"):
            list_1.reverse()
        elif(o[0::6] == "print"):
            print(list_1)
        else:
            pass
            
solve()
