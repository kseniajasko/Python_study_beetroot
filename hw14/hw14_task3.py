# Write a function called `choose_func` which takes a list of nums and 2 callback functions. If all
# nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

def choose_func(nums: list, func1, func2):
    b = False
    for a in nums:
        if a < 0:
            b = True
            break
    if b == False:
        return func1(nums)
    else:
        return func2(nums)


def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

nums_1 = [1, 2, 3, 4, 5]
nums_2 = [1, -2, 3, -4, 5]

print(choose_func(nums_1, square_nums, remove_negatives))
print(choose_func(nums_2, square_nums, remove_negatives))


# def choose_func(nums: list, func1, func2):
#     if len(nums) == len([i for i in nums if i > 0]):
#         return func1(nums)
#     else:
#         return func2(nums)