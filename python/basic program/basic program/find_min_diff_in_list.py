def solve(li):
    min_till_now = 99999*999
    for i in range(len(li)-1):
        diff = abs(li[i+1] - li[i])
        min_till_now = min(min_till_now,diff)
    return min_till_now

if __name__ == '__main__':
    li = []
    for i in range(int(input())):
        li.append(int(input()))
    
    result = solve(li)
    print(result)