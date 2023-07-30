def solve(li):
    result = []
    for i in range(len(li)):
        if li[i] == '+':
            first = int(li[i-2])
            second = int(li[i-1])
            
            result.append(first+second)
            #1 2 +
            #0 1 2
            li.pop(i-2)
            
    return result
    

if __name__ == '__main__':
    li = []
    for i in range(int(input())):
        li.append(input())
    result = solve(li)
    print(result)