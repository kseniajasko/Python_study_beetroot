#Task 1

#Write a function called oops that explicitly raises an IndexError exception when called. Then write another function that calls oops inside a try/except statement to catch the error. What happens if you change oops to raise KeyError instead of IndexError?
def oops(*args):
    raise IndexError
    
def oops_1():
    try:
        oops()
    except Exception as e:
        print('Exception catched')
        
oops_1()


#Task 2

#Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).



def cal(a, b):
    try:
        a = int(a)
        b = int(b)
        print(a**2/b)
    except ZeroDivisionError:
        print('Division by zero!')
    except ValueError:
        print('That was no valid number.')

cal(input('a = '), input('b = '))
