# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

def our_decorator(func):
    def function_wrapper(*args):
        print(f'Function name is {func.__name__} and arguments {args}')
    return function_wrapper

@our_decorator
def foo(x):
    print("It is " + x)

foo(42, 'dfgh')