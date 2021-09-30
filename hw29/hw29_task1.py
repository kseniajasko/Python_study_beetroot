# A bubble sort can be modified to “bubble” in both directions.
# The first pass moves “up” the list and the second pass moves “down.”
# This alternating pattern continues until no more passes are necessary.
# Implement this variation and describe under what circumstances it might be appropriate.
import random


# def bubble_sort(array):
#     n = len(array)
#     for k in range(n - 1, 0, -1):
#         for l in range(k):
#             if array[l] > array[l + 1]:
#                 array[l], array[l + 1] = array[l + 1], array[l]

def shaker_sort(array):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1

    while swapped is True:

        swapped = False
        # from left to right
        for k in range(start, end):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
                swapped = True
        # if not exchanges
        if not swapped:
            break

        swapped = False

        end -= 1
        # from right to left
        for l in range(end - 1, start-1, -1):
            if array[l] > array[l + 1]:
                array[l], array[l + 1] = array[l + 1], array[l]
                swapped = True

        start += 1


if __name__ == "__main__":
    test_list = [random.randint(1, 100) for _ in range(10)]
    print(test_list)
    copy_test_list = test_list[:]
#    bubble_sort(copy_test_list)
    shaker_sort(copy_test_list)
    print(copy_test_list)
