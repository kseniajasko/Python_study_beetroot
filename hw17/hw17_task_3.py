# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

class MyIterable:
    def __init__(self, list_1):
        self.list_1 = list_1
        self.current = 0

    def __iter__(self):
        return self

    def __getitem__(self, index):
        return (f'{index} of element {self.list_1[index]}')

    def __next__(self):
        if self.current > len(self.list_1)-1:
            raise StopIteration
        else:
            self.current += 1
            return self.list_1[self.current - 1]

    def add(self):
        self.list_1 = ['not-'+i  if len(i) <= 15 else i for i in self.list_1]
        return self.list_1

c = MyIterable(['kj', '88885khv', 'fsagag', 'dgh', 'lshlshm'])

print(next(c))
print(next(c))

print(c[0])
print(c[-1])
#print(c[0:5:2])

for k in range(1, 5):
    print((k, c.add()))





