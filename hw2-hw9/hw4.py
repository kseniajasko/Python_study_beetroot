#task_1
#Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.
# Sample String: 'helloworld'
#Expected Result : 'held'
#Sample String: 'my'
#Expected Result : 'mymy'
# Sample String: ' x'
# Expected Result: Empty String
# Tips:
# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string and negative indexing to get the last characters

s = input()

if len(s) < 2:
    print('')
elif len(s) == 2:
    print(s)
else:
    print(s[:2] + s[-2:])

#task_2
#Make a program that checks if a string is in the right format for a phone number. The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.

ph_num = input()
if len(ph_num) == 10:
    if ph_num.isdigit():
         print(f'That is phone number')
    else:
         print(f'That isn\'t phone number')
else:
     print(f'That isn\'t phone number')

#task_3
#Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. The program should check if your input is equal to the stored name even if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”, it should return True.
name_default = 'Oksana'
name_input = input()

if name_input.lower() == name_default.lower():
   print(True)
else:
    print(False)