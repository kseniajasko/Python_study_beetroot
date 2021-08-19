# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
# # Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
# and performs talk method on input parameter.

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return

    def simple_talk(self):
        self.talk()

class Cat(Animal):
    def talk(self):
        print('Meow!')

class Dog(Animal):
    def talk(self):
        print('Woof!')

a = Cat('Sirko')
b = Dog('Bob')
list1 = [a, b]

for animal in list1:
    animal.simple_talk()