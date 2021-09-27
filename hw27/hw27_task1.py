# Extend UnorderedList

# Implement append, index, pop, insert methods for UnorderedList.
# Also implement a slice method, which will take two parameters `start` and `stop`,
# and return a copy of the list starting at the position and going up to but not including
# the stop position.

from node import Node

class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self._head
        found = False

        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def pop(self):
        current = self._head
        previous = None

        if current is None:
            return "No item in list"

        while current.get_next() is not None:
            previous = current
            current = current.get_next()

        previous.set_next(None)
        return current.get_data()


    # insert item in the pos-th of the list
    def insert_of_position(self, pos, item):
        current = self._head
        previous = None
        index = 0
        temp = Node(item)

        while current is not None and index < pos:
            previous = current
            current = current.get_next()
            index += 1

        if pos == 0:
            temp.set_next(self.head)
            self._head = temp
        else:
            if current is None:
                previous.setNext(temp)
            else:
                temp.setNext(current)
                previous.setNext(temp)

    # remove item from the pos-th of the list
    def delete_from_position(self, pos):
        current = self._head
        previous = None
        index = 0

        if current is None:
            return "No item in list"

        while index < pos and current is not None:
            previous = current
            current = current.get_next()
            index += 1

        if current is None:
            return "No item in list"
        else:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.setNext(current.get_next())
            return current.get_data()

    def insert(self, item):
        current = self._head
        previous = None
        temp = Node(item)

        if current is None:
            previous.set_next(temp)

        temp.set_next(self._head)
        self._head = temp
        return current.get_data()

    def index(self, item):
        current = self._head
        found = False
        index = 0

        while current is not None and not found:
            if current.get_data() != item:
                index += 1
                current = current.get_next()
            else:
                found = True

        if found:
            return f'Element {item} has index {index}'
        else:
            return "Not Found"

    def generator_list(self):
        temp = self._head

        while temp is not None:
            yield temp.get_data()
            temp = temp.get_next()

    def slice(self, start = None, end = None):
        current = [i for i in self.generator_list()]

        if start is None or end is None:
            raise ValueError('Enter start and end')
        elif start < 0 or start > end or end > len(current)-1:
            raise ValueError('Wrong start or/and end')
        else:
            return current[start:end]

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation +">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.pop())
    print(my_list.insert(111))
    print(my_list.insert(103))
    print(my_list)
    print(my_list.pop())
    print(my_list)
    print(my_list.index(54))
    print(my_list.slice(2, 5))



