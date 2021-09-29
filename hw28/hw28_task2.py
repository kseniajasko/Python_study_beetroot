# Read about the Fibonacci search and implement it using python. Explore its complexity
# and compare it to sequential, binary searches.

# Differences with Binary Search:
# 1. Fibonacci Search divides given array in unequal parts
# 2 . Binary Search uses the division operator to divide range.
# Fibonacci Search doesn’t use /, but uses + and -. The division operator may be costly on some CPUs.
# 3. Fibonacci Search examines relatively closer elements in subsequent steps. So when the input array is big that cannot fit in CPU cache or even in RAM, Fibonacci Search can be useful.

# The time complexity for Fibonacci search is O(log n); the same as binary search.
# This means the algorithm is faster than both linear search and jump search in most cases.

import timeit

def fibonacci_generator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_generator(n - 1) + fibonacci_generator(n - 2)


def fibonacci_search(arr, x):
    m = 0
    while fibonacci_generator(m) < len(arr):
        m = m + 1
    offset = -1
    while fibonacci_generator(m) > 1:
        i = min(offset + fibonacci_generator(m - 2) , len(arr) - 1)
#        print(f'Current element {i}: {arr[i]}')
        if x > arr[i]:
            m = m - 1
            offset = i
        elif x < arr[i]:
            m = m - 2
        else:
            return i
    if fibonacci_generator(m - 1) and arr[offset + 1] == x:
        return offset + 1
    return -1

#print('Number found at index : ', fibonacci_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6))

def sequential_search(array, item):
    pos = 0
    found = False
    while pos < len(array) and not found:
        if array[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def binary_search(array, item):
    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            found = True
        else:
            if item < array[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

# if __name__ == "__main__":
#     seq_timer = timeit.timeit(
#         stmt="sequential_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6)",
#         number=10,
#         setup="from __main__ import sequential_search"
#     )
#     print(seq_timer)
#
#     bin_timer = timeit.timeit(
#         stmt="binary_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6)",
#         number=10,
#         setup="from __main__ import binary_search"
#     )
#     print(bin_timer)
#
#     bin_timer = timeit.timeit(
#         stmt="fibonacci_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6)",
#         number=10,
#         setup="from __main__ import fibonacci_search"
#     )
#     print(bin_timer)

