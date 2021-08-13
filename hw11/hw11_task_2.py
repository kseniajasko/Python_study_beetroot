# Task 2
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:
    list_1 = []

    def __init__(self, list_1):
        if self.is_empty_list(list_1):
            print('Empty list')
            return
        self.list_1 = list_1

    def is_empty_list(self, list):
        return True if not list or len(list) == 0 else False

    def square_nums(self):
        if self.is_empty_list(self.list_1):
            print("Error, cann't square, empty list")
            return

        a = [i ** 2 for i in self.list_1]
        return print(a)

    def remove_positives(self):
        if self.is_empty_list(self.list_1):
            print("Error, empty list")
            return

        a = [i for i in self.list_1 if  i < 0]
        return print(a)

    def filter_leaps(self):
        if self.is_empty_list(self.list_1):
            print("Error, empty list")
            return

        a = [i for i in self.list_1 if not i % 4 and i > 0]
        return print(a)

m = Mathematician([-2000, 2004, -2005, -1])
#m = Mathematician([])

m.square_nums()
m.filter_leaps()
m.remove_positives()