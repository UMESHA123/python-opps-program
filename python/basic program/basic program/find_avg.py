def solve(dict_data,find_avg):
    for k,v in dict_data.items():
        if k == find_avg:
            return sum(v)/len(v)

if __name__ == '__main__':
    dict_data = {}
    for i in range(int(input())):
        name = input()
        score = []
        for i in range(3):
            score.append(int(input()))
        dict_data[name] = score
    find_avg = input()
    result = solve(dict_data,find_avg)
    
    print(result)    
        