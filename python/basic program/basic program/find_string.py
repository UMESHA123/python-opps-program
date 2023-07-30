#the startwith is a method which check the given text
#with the stentance if it found it return the true else false
#find_text or sub string
def solve(text,find_text):
    count = 0
    for i in range(len(text)):
        if text[i:].startswith(find_text):
            count = count + 1
    return count
if __name__ == '__main__':
    text = input()
    find_text = input()
    result = solve(text,find_text)
    print(result)
    