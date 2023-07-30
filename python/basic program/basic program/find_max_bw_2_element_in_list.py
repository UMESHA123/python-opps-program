def solve(li):
    max_till_now = 0
    for i in range(len(li)-1):
        diff = abs(li[i+1] - li[i])
        max_till_now = max(max_till_now,diff)
    return max_till_now

if __name__ == '__main__':
    li = []
    for i in range(int(input())):
        li.append(int(input()))
    
    result = solve(li)
    print(result)