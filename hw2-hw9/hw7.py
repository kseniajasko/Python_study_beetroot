#TASK_1
#Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.
def word_dict(str):
    dict_1 = dict()
    keys = str.split()
    for key in keys:
        if key in dict_1:
            dict_1[key] += 1
        else:
            dict_1[key] = 1
    return dict_1
# sentence_1 = input('Введіть речення: ')
# print(word_dict(sentence_1))



#TASK_2
# Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock.
def returnSum(dict_1, dict_2):
    sum = 0
    value_dict_1 = []
    value_dict_2 = []
    
    for value_1 in dict_1.values():
        value_dict_1.append(value_1)

    for value_2 in dict_2.values():
        value_dict_2.append(value_2)

    l = len(value_dict_1)-1
    i = 0
    while i <= l:
        prod = value_dict_1[i]*value_dict_2[i]
        sum += prod
        i += 1
    return sum



stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

print(f'Total price: {returnSum(stock, prices)}')



#TASK_3
#Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
list_1 = [(i, i*i) for i in range(1, 11)]
print(list_1)

