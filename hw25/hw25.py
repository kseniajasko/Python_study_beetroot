from typing import Optional, Union

#TASK_1
def to_power(x: Union[int, float], exp: int) -> Union[int, float]:

    if exp < 0:
        raise ValueError('This function works only with exp > 0.')

    if exp == 0:
        return 1

    return x * to_power(x, exp-1)
#print(to_power(2.3, 4))
#print(to_power(2, -4))

#TASK_2
def is_palindrome(looking_str: str, index: int = 0) -> bool:

    s = looking_str.lower().strip()
    l = len(s)

    if l < 2:
        return True

    elif s[index] == s[l - 1]:
        return is_palindrome(s[index+1: l - 1])

    else:
        return False
#
# print(is_palindrome('Sasas'))
# print(is_palindrome('mom'))
# print(is_palindrome(' '))
# print(is_palindrome('k'))

#TASK_3

def mult(a: int, n: int) -> int:

    if n < 0:
        raise ValueError('This function works only with positive integers')

    if n == 0:
        return 0

    return a + mult(a, n-1)

# print(mult(2, 4))
# print(mult(2, 0))
# print(mult(2, -4))

#TASK_4
def reverse(input_str: str) -> str:

    if len(input_str) == 0:
        raise ValueError('Empty string')

    else:
        return reverse(input_str[1:])+input_str[0]

# print(reverse('hello'))
# print(reverse('o'))
# print(reverse(''))

#TASK_5
def sum_of_digits(digit_string: str) -> int:

    n = len(digit_string.split())

    if n == 0:
        return 0

    if not digit_string.isdigit():
        raise ValueError('input string must be digit string')

    list_1 = [int(c) for c in digit_string]

    return list_1[-1] + sum_of_digits(digit_string[: -1])

# print(sum_of_digits('12345'))
# print(sum_of_digits('test'))