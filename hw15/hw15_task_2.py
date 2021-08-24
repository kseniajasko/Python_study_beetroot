# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you
# to add workers to a Boss. You're not allowed to add instances of Boss class to
# workers list directly via access to attribute, use getters and setters instead!
# You can refactor the existing code.

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def __repr__(self):
        return f'({self.id}, {self.name}, {self.company})'

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, obj):
        if not isinstance(obj, Worker):
            raise TypeError('WorkersError')
        else:
            self._workers.append({'id': obj.id, 'name': obj.name, 'company': obj.company})

class Worker:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.company}, {self.boss}'

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise TypeError('Boss error')
            return

        if self._boss:
            temp_1 = next((a for a in self._boss.workers if a['id'] == self.id), None)
            if temp_1:
                self._boss.workers.remove(temp_1)
        new_boss.workers = self
        self._boss = new_boss

b_1 = Boss(1, 'Alex', 'MMM')
b_2 = Boss(2, 'Henk', 'OOO')
w_1 = Worker(1, 'John', 'C')
w_2 = Worker(2, 'Jeck', 'RO')
w_3 = Worker(3, 'Sam', 'VO')
w_1.boss = b_1
w_2.boss = b_1
w_3.boss = b_1
print(b_1.workers)
print(b_2.workers)
w_2.boss = b_2
print(b_1.workers)
print(b_2.workers)

