string validation:

isalnum --> to validate the string contain the both number and the string.

isalpha --> this function are used to validate the given string is alphabet are not

isdigit() --> this function are used to validate the given string is digit pr not

islower() --> is function are used to find the given string is lower or not if lower then it return the true else it return false.

isupper() --> this function are used to find the given string is upper or not if uppper this will return the true else it return the false.




#capitalize program

string = "alison heck"
n = string.split() #we need tp store it in the onther variable because the original list are not modified afterwe performing the split function.
new_list = []
for item in n:
    first_letter = item[0]
    second_string = item[1::]
    if first_letter.islower():
        first_letter = first_letter.upper()
        updated_item = first_letter + second_string
    else:
        updated_item = first_letter
    new_list.append(updated_item)
print(' '.join(new_list))
    
    
    
    output:
    
    Alison Heck


