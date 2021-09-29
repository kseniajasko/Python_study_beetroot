# Implement binary search using recursion.

def binary_search(my_list, low, high, elem):
    if high >= low:
        mid = (high + low) // 2
        print(mid)
        if my_list[mid] == elem:
            return mid
        elif my_list[mid] > elem:
            return binary_search(my_list, low, mid - 1, elem)
        else:
            return binary_search(my_list, mid + 1, high, elem)
    else:
        return -1


my_list = [i for i in range(0,10)]
elem_to_search = 9
print(f"The list is {my_list}")

my_result = binary_search(my_list, 0, len(my_list) - 1, elem_to_search)

if my_result != -1:
    print("Element found at index ", str(my_result))
else:
    print("Element not found!")