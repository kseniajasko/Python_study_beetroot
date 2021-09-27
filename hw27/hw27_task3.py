#Implement a queue using a singly linked list.

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    # Method to add an item to the queue
    def add_queue(self, item):
        temp = Node(item)

        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # Method to remove an item from queue
    def del_queue(self):

        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

    def __repr__(self):
        representation = "<Queue: "
        current = self.front
        while current is not None:
            representation += f"{current.data} "
            current = current.next
        return representation +">"

    def __str__(self):
        return self.__repr__()


if __name__== '__main__':
    q = Queue()
    q.add_queue(10)
    q.add_queue(20)
    # q.del_queue()
    # q.del_queue()
    q.add_queue(30)
    q.add_queue(40)
    q.add_queue(50)
    q.del_queue()
    print(q)
    print("Queue Front: " + str(q.front.data))
    print("Queue Rear: " + str(q.rear.data))