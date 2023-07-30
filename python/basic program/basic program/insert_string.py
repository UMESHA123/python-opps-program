def solve(text,position,letter):
    left_text = text[0:position]
    right_text = text[position+1:]
    result = left_text + letter + right_text
    return result

if __name__ == '__main__':
    text = input()
    position = int(input())
    letter = input()
    result = solve(text,position,letter)
    print(result)