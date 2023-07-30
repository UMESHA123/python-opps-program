def print_formatted(number):
    # your code goes here
    num_len_decimal = len(str(number))
    n = bin(number)
    n = n[2:]
    num_len_bin = len(str(n))
    for num in range(1,number+1):
        num = str(num)
        oct_num = oct(int(num))
        oct_num = oct_num[2:]
        #print(oct_num)
        hex_num = hex(int(num))
        
        hex_num = hex_num[2:]
        #print(hex_num)
        binary_num = bin(int(num))
        binary_num = binary_num[2:]
        for i in range(1):
            num = str(num)
            if len(num) < num_len_decimal:
                
                space_add = num_len_decimal - len(num)
                result = ''
                for _ in range(space_add):
                    result = result + ' '
                result = ' ' +result + num
                print(result,end="")
            else:
                result = ' ' + num  
                print(result,end='')
                
            if len(oct_num) < num_len_decimal:
                space_add = num_len_decimal - len(oct_num)
                result = ''
                for _ in range(space_add):
                    result = result + ' '
                result ='  ' + result + oct_num
                print(result,end="")
            else:
                result =  '  ' +oct_num  
                print(result,end='')
                       
            if len(hex_num) < num_len_decimal:
                space_add = num_len_decimal - len(hex_num)
                result = ''
                for _ in range(space_add):
                    result = result + ' '
                result ='  ' + result + hex_num
                
                print(result,end ='')
            else:
                result = '  ' + hex_num  
                print(result,end ='')        
                    
            if len(binary_num) < num_len_bin:
                space_add = num_len_bin - len(binary_num)
                result = ''
                for _ in range(space_add):
                    result = result + ' '
                result = '  ' +result + binary_num
                print(result,end="")
            else:
                result = '  ' + binary_num 
                print(result,end='')        
        
        print('')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)