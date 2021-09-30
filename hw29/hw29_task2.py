# Implement the mergeSort function without using the slice operator.
import random
# without the slice operator
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted

def merge_sort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print(f"Given array is {arr}")

merge_sort(arr, 0, n - 1)
print(f"Sorted array is {arr}")






# with the slice operator
# def merge_sort(array):
#     if len(array) > 1:
#         mid = len(array) // 2
#
#         left_half = array[:mid]
#         right_half = array[mid:]
#
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         i = 0
#         j = 0
#         k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] <= right_half[j]:
#                 array[k] = left_half[i]
#                 i = i + 1
#             else:
#                 array[k] = right_half[j]
#                 j = j + 1
#             k = k + 1
#
#         while i < len(left_half):
#             array[k] = left_half[i]
#             i = i + 1
#             k = k + 1
#
#         while j < len(right_half):
#             array[k] = right_half[j]
#             j = j + 1
#             k = k + 1
#
# if __name__ == "__main__":
#     test_list = [random.randint(1, 100) for _ in range(10)]
#     print(test_list)
#     copy_test_list = test_list[:]
#     merge_sort(copy_test_list)
#     print(copy_test_list)
