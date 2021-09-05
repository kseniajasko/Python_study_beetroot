# Create your own implementation of a built-in function enumerate, named `with_index`,
# which takes two parameters: `iterable` and `start`, default is 0.
# Tips: see the documentation for the enumerate function

def with_index(iterable = 0, start = 0):
    list_0 = []
    if iterable == 0:
        return [(start, iterable)]

    for i in iterable:
        list_0.append((start, i))
        start += 1
    return list_0

a = ['gdh', 'agg', 25, 36]
print(with_index(a))



