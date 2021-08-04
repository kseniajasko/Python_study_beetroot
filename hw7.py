
# TASK_1
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. The function should then print “My favorite movie is named {name}”.

def favorite_movie(name):
     if  name.strip():
         print(f'My favorite movie is named {name}')
     else:
         favorite_movie(input('Enter your favorite movie: '))

favorite_movie('')


# TASK_2
# Create a function called make_country, which takes in a country’s name and capital as parameters. Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(**kwargs):
    return print(kwargs)

make_country(German = 'Berlin', Ukraine = 'Kyiv')

# TASK_3
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42


def make_operation(*args):
    if '+' in args:
        print(sum(args[1:]))

    elif '-' in args:
       print(args[1] - sum(args[2:]))

    elif '*' in args:
        res = 1
        for a in args[1:]:
            res *= a
        print(res)

    elif '/' in args:
        res = args[1]
        for a in args[2:]:
            res /= a
        print(res)

make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 7, 2, 5)
make_operation('/', 2, 3)