letters = input("Enter the upper and lower data")
updated_data = ""
for letter in letters:
    if letter == " ":
        pass
    elif letter.islower():
        updated_data = updated_data + letter.upper()
    elif letter.isupper():
        updated_data = updated_data + letter.lower()
    else:
        updated_data = updated_data + letter
print(updated_data)
