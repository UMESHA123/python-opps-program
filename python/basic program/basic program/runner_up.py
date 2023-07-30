def solve(num_list):
    num_list = list(set(num_list))
    num_list.sort()
    return num_list[-2]


if __name__ == '__main__':
    num_list = []
    num = int(input())
    for _ in range(num):
        num_list.append(int(input()))
    result = solve(num_list)
    print(result)