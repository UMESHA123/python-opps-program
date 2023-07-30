def solve(text,num):
    div_len = int(len(text)/num)
    div_text = []
    left = 0
    right = div_len
    
    while right != len(text)+div_len:
        div_text.append(text[left:right])
        left = right
        right = right + div_len 
    
    sub_str_list = []
  
    for sub_str in div_text:
        temp_str =''
        for letter in sub_str:
            if letter not in temp_str:
                temp_str = temp_str + letter
        sub_str_list.append(temp_str)
        
    return sub_str_list 


if __name__ == '__main__':
    text = input()
    num = int(input())
    result = solve(text,num)
    for sub_str in result:
        print(sub_str)