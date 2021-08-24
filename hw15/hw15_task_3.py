from functools import wraps

class TypeDecorators:
    def to_int(f):
        @wraps(f)
        def wrapper(x):
            try:
                return int(f(x))
            except ValueError:
                return None
        return wrapper

    def to_str(f):
        @wraps(f)
        def wrapper(x):
            try:
                return str(f(x))
            except ValueError:
                return None
        return wrapper

    def to_float(f):
        @wraps(f)
        def wrapper(x):
            try:
                return float(f(x))
            except ValueError:
                return None
        return wrapper

    def to_bool(f):
        @wraps(f)
        def wrapper(*args):
            try:
                return bool(f(args))
            except ValueError:
                return None
        return wrapper

@TypeDecorators.to_int
def do_int(x):
    return x

@TypeDecorators.to_str
def do_str(x):
    return x

@TypeDecorators.to_float
def do_float(x):
    return x

@TypeDecorators.to_bool
def do_bool(x):
    return x

print(do_int('25'))
print(type(do_int('25')))

print(do_str(25))
print(type(do_str(25)))

print(do_float('25'))
print(type(do_float('25')))

print(do_bool('**', 'fjsg'))
print(type(do_bool('**')))