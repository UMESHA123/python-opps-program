def solve(text):
    result = []
    if text.isalnum():
        result.append(True)
    else:
        result.append(False)
    if text.isdigit():
        result.append(True)
    else:
        result.append(False)
    if text.isalpha():
        result.append(True)
    else:
        result.append(False)
    if text.isupper():
        result.append(True)
    else:
        result.append(False)
    if text.islower():
        result.append(True)
    else:
        result.append(False)
    return result 

if __name__ == '__main__':
    text = input()
    result = solve(text)
    print(result)