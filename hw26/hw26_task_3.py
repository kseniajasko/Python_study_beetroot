# Extend the Stack to include a method called get_from_stack that searches and returns an element e
# from a stack. Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

# Extend the Queue to include a method called get_from_stack that searches and returns an element e
# from a queue. Any other element must remain in the queue respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

# 1
class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def get_from_stack(self, item):
        if item in self._items:
            return item
        else:
            raise ValueError('Not exist in stack')

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

# if __name__ == "__main__":
#     s = Stack()
#     print(s.is_empty())
#     s.push(4)
#     s.push('dog')
#     s.push('cat')
#     print(s)
#
#     print(s.get_from_stack('cat'))

# 2
class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def get_from_stack(self, item):
        if item in self._items:
            return item
        else:
            raise ValueError('Not exist in queue')

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


# if __name__ == "__main__":
#     q = Queue()
#     q.enqueue(4)
#     q.enqueue('dog')
#     q.enqueue(True)
#     print(q)
#     print(q.get_from_stack('dog'))
