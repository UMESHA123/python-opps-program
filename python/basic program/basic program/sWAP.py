def solve(text):
    result = ''
    for letter in text:
        if letter.islower():
            result += letter.upper()
        elif letter.isupper():
            result +=letter.lower()
        else:
            result += letter
    return result

if __name__ == '__main__':
    text = input()
    result = solve(text)
    print(result)