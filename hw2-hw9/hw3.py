#task_1
# Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

#“Good day < name >! < day > is a perfect day to learn some python.”

#Note that < name > and < day > are predefined variables in source code. An additional bonus will be to use different string formatting methods for constructing result string.
#1
name = 'Oksana'
day = 'Saturday'
print(f'Good day {name}! {day} is a perfect day to learn some python.')

#2
s = 'Good day {}! {} is a perfect day to learn some python.'
print(s.format(name, day))

#3
print('Good day {0}! {1} is a perfect day to learn some python.'.format(name, day))

#4
print('Good day %s! %s is a perfect day to learn some python.' % (name, day))

#task_2
#Save your first and last name as separate variables, then use string concatenation to add them together with a white space in between and print a greeting.
f_name = 'Oksana'
l_name = 'Satur'
print(f_name + ' ' + l_name)
print('Hello! My name is ' + f_name + ' ' + l_name + '.')

#task_3
# Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: Addition, Subtraction, Division, Multiplication, Exponent (Power), Modulus, Floor division
a = 36
b = 5

c = a + b
d = a - b
k = a / b
e = a * b
f = a ** b
m = abs(b-a)
l = a // b
n = a % b
print(c, d, k, e, f, m, l, n, sep = '\n')