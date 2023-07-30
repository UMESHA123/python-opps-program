def solve(all_one_in_func_list):
    result_list = []
    for func in all_one_in_func_list:
        if func[0:6] == 'insert':
            first = int(func[7])
            second = int(func[9:])
            result_list.insert(first,second)
        elif func == 'print':
            print(result_list)
        elif func[0:6] == 'append':
            append_value = int(func[-1])
            result_list.append(append_value)
        elif func[0:6] == 'remove':
            remove_value = int(func[-1])
            result_list.remove(remove_value)
        elif func == 'sort':
            result_list.sort()
        elif func == 'pop':
            result_list.pop()
        elif func == 'reverse':
            result_list.reverse()
        
            

if __name__ == '__main__':
    all_one_in_func_list = []
    for i in range(int(input())):
        all_one_in_func_list.append(input())
    result = solve(all_one_in_func_list)