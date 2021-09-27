# Implement a stack using a singly linked list.

class Node:
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # head is default NULL
    def __init__(self):
        self.head = None

    # Checks if stack is empty
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # Method to add data to the stack
    # adds to the start of the stack
    def push(self, data):

        if self.head is None:
            self.head = Node(data)

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # Remove element that is the current head (start of the stack)
    def pop(self):

        if self.is_empty():
            return None

        else:
            # Removes the head node and makes
            # the preceeding one the new head
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    # Returns the head node data
    def peek(self):

        if self.is_empty():
            return None

        else:
            return self.head.data

    # Prints out the stack
    def display(self):

        iter_node = self.head
        if self.is_empty():
            print("Stack Underflow")

        else:

            while iter_node is not None:
                print(iter_node.data, "->", end=" ")
                iter_node = iter_node.next
            return

    def __repr__(self):
        representation = "<Stack: "
        current = self.head
        while current is not None:
            representation += f"{current.data} "
            current = current.next
        return representation +">"

    def __str__(self):
        return self.__repr__()

my_stack = Stack()

my_stack.push(11)
my_stack.push(22)
my_stack.push(33)
my_stack.push(44)

print(my_stack)
# Display stack elements
my_stack.display()

# Print top element of stack
print("\nTop element is ", my_stack.peek())

# Delete top elements of stack
my_stack.pop()
my_stack.pop()

# Display stack elements
my_stack.display()

# Print top element of stack
print("\nTop element is ", my_stack.peek())