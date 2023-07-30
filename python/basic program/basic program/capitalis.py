def solve(text):
    result = ''
    text = text.split()
    for word in text:
        first_letter = word[0]
        second_letter = word[1:]
        first_letter = first_letter.upper()
        result = result + first_letter + second_letter + ' '
    return result
 

if __name__ == '__main__':
    text = input()
    result = solve(text)
    print(result)