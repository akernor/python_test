class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=100):
        Person.giveRaise(self, percent + bonus)


ivan = Person('Ivan Petrov')
print(ivan)

john = Person('John Sidorov', job = 'dev', pay = 100000)
print(john)
print(ivan.lastName(), john.lastName())

john.giveRaise(.10)
print(john)

tom = Manager('Tom Jones', 50000)
tom.giveRaise(.10)
print(tom.lastName())
print(tom)




