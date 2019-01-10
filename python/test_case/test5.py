# first test
# class Person:
#     name = "Ivan"
#     age = 10
#
#     def set(self, name, age):
#         self.name = name
#         self.age = age
#
#
# vlad = Person()
# vlad.set("Влад", 25)
# print(vlad.name + " " + str(vlad.age))
#
# ivan = Person()
# ivan.set("Иван", 56)
# print(ivan.age)
#
# kolya = Person()
# kolya.set(kolya.name, kolya.age)
# print(kolya.name + " " + str(kolya.age))



# secont test
# class User:
#     def setName(self, n):
#         self.name = n
#
#     def getName(self):
#         try:
#             return self.name
#         except:
#             print("No name")
#
#
# first = User()
# second = User()
#
# first.setName("Bob")
#
# print(first.getName())
# print(second.getName())

# static class
# class SomeClass:
#     @staticmethod
#     def hello():
#         print("Hello, world")
#
#
# SomeClass.hello()
# obj = SomeClass()
# obj.hello()
#
#
# # class method
# class SomeClass:
#     @classmethod
#     def hello(cls):
#         print('Hello, class {}'.format(cls.__name__))
#
#
# SomeClass.hello()


# class Elevator:
#     """ Simple elevator class """
#     people_lifted = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.people_lifted = 0
#
#     def lift(self):
#         print("{} lifted someone".format(self.name))
#         self.people_lifted += 1
#         Elevator.people_lifted += 1
#
#     def info(self):
#         print(self.name, "lifted", self.people_lifted, "people out of", Elevator.people_lifted)
#
#
# elevator_1 = Elevator("OTIS")
# elevator_2 = Elevator("PHILLIPS")
#
# elevator_1.lift()
# elevator_2.lift()
# elevator_2.lift()
# elevator_1.info()
# elevator_2.info()


# наследование
# class Tree:
#     def __init__(self, kind, height):
#         self.kind = kind
#         self.age = 0
#         self.height = height
#
#     def info(self):
#         """ Метод вывода информации о дереве """
#         print("{} years old {}. {} meters high.".format(self.age, self.kind, self.height))
#
#     def grow(self):
#         """ Метод роста """
#         self.age += 1
#         self.height += 0.5
#
#
# class FruitTree(Tree):
#     def __init__(self, kind, height):
#         super().__init__(kind, height)
#
#     def give_fruits(self):
#         print("Collected 20kg of {}s".format(self.kind))
#
#
# tree_1 = Tree('oak', 0.5)
# tree_1.info()
# tree_1.grow()
# tree_1.info()
#
# tree_2 = FruitTree('apple', 0.7)
# tree_2.info()
# tree_2.grow()
# tree_2.give_fruits()
# # tree_1.give_fruits() #error


# class Robot:
#
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('(Инициализация {0})'.format(self.name))
#
#         Robot.population += 1
#
#     def __del__(self):
#         print('{0} уничтожается!'.format(self.name))
#
#         Robot.population -= 1
#
#         if Robot.population == 0:
#             print('{0} был последним.'.format(self.name))
#         else:
#             print('Осталось {0:d} работающих роботов.'.format(Robot.population))
#
#     def sayHi(self):
#         print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
#
#     @staticmethod
#     def howMany():
#         print('У нас {0:d} роботов.'.format(Robot.population))
#
#     howMany = staticmethod(howMany)
#
#
# rob_1 = Robot('wally')
# rob_1.sayHi()
# Robot.howMany()
# rob_2 = Robot('Zuz')
# rob_2.sayHi()
# Robot.howMany()
# del rob_2
# del rob_1
# Robot.howMany()


class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Created SchoolMember: {0})'.format(self.name))
    def tell(self):
        print('Name:"{0}" Age:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Created Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Created Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{0:d}"'.format(self.marks))

t = Teacher('Ms. Petrova', 55, 3000)
s = Student('Kolya Pertuch', 12, 85)
print()
t.tell()
s.tell()