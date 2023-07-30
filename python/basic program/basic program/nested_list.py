#00 01
#10 11
#20 21
#30 31

def solve(num,neasted_list):
    result_list = []
    score_list = []
    for i in range(num):
        score_list.append(neasted_list[i][1])
    score_list.sort()
    second_min = score_list[1]
    print(second_min)
    for j in range(num):
        if second_min == neasted_list[j][1]:
            result_list.append(neasted_list[j][0])
    result_list.sort()
    return result_list   

if __name__ == '__main__':
    num = int(input())
    neasted_list = []

    for i in range(num):
        name = input()
        score = float(input())
        neasted_list.append([name,score])

    result = solve(num,neasted_list)
    for item in result:
        print(item)