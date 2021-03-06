import turtle as t

class Shape:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw_shape(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Circle(Shape):

    def draw_shape(self):
        t.setx(self.x)
        t.setx(self.y)
        t.down()
        t.circle(self.radius)
        t.up()

class Square(Shape):
    def draw_shape(self):
        t.setx(self.x)
        t.setx(self.y)
        t.down()
        t.forward(self.radius*2)
        t.right(90)
        t.forward(self.radius*2)
        t.right(90)
        t.forward(self.radius*2)
        t.right(90)
        t.forward(self.radius*2)
        t.right(90)
        t.up()

my_square1 = Square(0, 0, 25)
my_circle = Circle(25, 25, 25)
my_square2 = Square(0, 0, 50)
my_square1.draw_shape()
my_circle.draw_shape()
#my_square2.draw_shape()
t.done()