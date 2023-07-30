def solve(li,find_sum):
    li.sort()
    left = 0
    right = len(li)-1
    print(right)
    result_index = []
    while left <= right:
        if li[left]+li[right] < find_sum:
            left = left + 1
        elif li[left] + li[right] > find_sum:
            right = right - 1
        elif li[left] + li[right] == find_sum:
            result_index.append([left,right])
            left = left + 1
            right = right - 1
    return result_index
            

if __name__ == '__main__':
    li = []
    for i in range(int(input())):
        li.append(int(input()))
    
    find_sum = int(input())
    result = solve(li,find_sum)
    print(result)