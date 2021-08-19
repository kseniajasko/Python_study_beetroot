# Write a Python program to access a function inside a function (Tips: use function, which returns another function)
# Ex_1
def test(a):
     def add(b):
          nonlocal a
          a += 1
          return a+b
     return add
c = test(4)
print(c(2))
print(c(10))
print(c(10))

# Ex_2
def f1():
     s = 'I love Python'

     def f2():
          nonlocal s
          s = 'You too'
          print(s)

     f2()
     print(s)

f1()